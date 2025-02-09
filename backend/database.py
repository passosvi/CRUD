#UNICA FUNÇÃO DESSE FILE É FAZER CONEXAO COM POSTGRES
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

# Criação do engine
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit =False, autoflush= False, bind=engine)

Base = declarative_base() #ORM

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#semelhante ao return, porém yield para a função








