from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models, schemas
from .database import SessionLocal, engine

# Garante que as tabelas sejam criadas no banco (se não existirem) quando a aplicação iniciar.
# Esta linha é lida uma vez na inicialização do módulo.
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Encurtador de URL")

# Configuração do CORS para permitir que o Frontend se comunique com o Backend.
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Função de Dependência para o Banco de Dados ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Lógica de Encurtamento (Base62) ---
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(ALPHABET)

def base62_encode(num: int) -> str:
    """Converte um ID numérico para uma string em base62."""
    if num == 0:
        return ALPHABET[0]
    
    arr = []
    while num:
        rem = num % BASE
        num = num // BASE
        arr.append(ALPHABET[rem])
    arr.reverse()
    return "".join(arr)

# --- Endpoints da API ---

@app.post("/shorten", response_model=schemas.URL, status_code=201)
def create_short_url(url: schemas.URLCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova URL encurtada, aceitando um apelido customizado opcional.
    """
    db_url = crud.create_db_url(db=db, url=url)

    # Cenário 1: Apelido customizado já está em uso.
    
    if db_url is None:
        raise HTTPException(
            status_code=400,
            detail="Este apelido customizado já está em uso. Tente outro."
        )

    # Cenário 2: Apelido customizado foi fornecido e usado com sucesso.
    
    if db_url.short_code:
        return db_url

    # Cenário 3: Nenhum apelido fornecido, gerar um automaticamente.
    
    short_code = base62_encode(db_url.id)
    updated_url = crud.update_short_code(db=db, url_id=db_url.id, short_code=short_code)
    
    return updated_url

@app.get("/{short_code}")
def redirect_to_long_url(short_code: str, db: Session = Depends(get_db)):
    """
    Redireciona para a URL longa e incrementa o contador de cliques.
    """
    db_url = crud.get_url_by_short_code(db, short_code=short_code)
    
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL não encontrada")
    
    db_url.clicks += 1
    db.commit()
    db.refresh(db_url)
    
    # Usa 302 (redirecionamento temporário) para garantir que o navegador sempre
    # consulte nossa API, permitindo a contagem de cliques.
    
    return RedirectResponse(url=db_url.long_url, status_code=302)

@app.get("/stats/{short_code}", response_model=schemas.URL)
def get_url_stats(short_code: str, db: Session = Depends(get_db)):
    """
    Retorna as estatísticas (incluindo cliques) de uma URL encurtada.
    """
    db_url = crud.get_url_by_short_code(db, short_code=short_code)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL não encontrada")
    return db_url