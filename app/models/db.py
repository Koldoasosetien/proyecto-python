# app/models/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# URL de conexión a la base de datos, en estecaso un archivo local.
DATABASE_URL = "sqlite:///biblioteca.db"


# Creación del motor de base de datos
# - check_same_thread=False desactiva que solo pueda un hilo por conexion.
engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False}
)

sessionFactory = sessionmaker(bind=engine)
session = scoped_session(sessionFactory)
