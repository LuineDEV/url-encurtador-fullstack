from sqlalchemy.orm import Session
from . import models, schemas

def get_url_by_short_code(db: Session, short_code: str):
    return db.query(models.URL).filter(models.URL.short_code == short_code).first()

# Função completamente reescrita para a nova lógica
def create_db_url(db: Session, url: schemas.URLCreate) -> models.URL | None:
    # Se o usuário forneceu um apelido customizado
    if url.short_code:
        # Verifica se o apelido já existe no banco
        if get_url_by_short_code(db, short_code=url.short_code):
            return None 
        # Cria a URL já com o apelido fornecido
        db_url = models.URL(long_url=url.long_url, short_code=url.short_code)
    else:
        # Cria a URL sem o short_code para gerar o ID primeiro 
        db_url = models.URL(long_url=url.long_url)

    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def update_short_code(db: Session, url_id: int, short_code: str):
    db_url = db.query(models.URL).filter(models.URL.id == url_id).first()
    if db_url:
        db_url.short_code = short_code
        db.commit()
        db.refresh(db_url)
    return db_url