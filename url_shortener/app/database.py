from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco de dados MySQL
# Formato: "mysql+mysqlconnector://user:password@host:port/database_name"
# Usar 'db' como host porque é o nome do serviço do MySQL no docker-compose
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:luinesenha123@db:3306/url_shortener_db"

# Cria o "motor" do SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cria uma fábrica de sessões. Cada sessão é uma conversa com o banco de dados.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Usar esta Base para criar nossos modelos de tabela do banco
Base = declarative_base()