# app/models/consultas.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Usuarios(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellidos = Column(String) 
    email = Column(String)
    password = Column(String)
    direccion = Column(String) 
    admin = Column(Boolean)

class Libro(Base):
    __tablename__ = 'libros'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    autor = Column(String)
    copias = Column(Integer)
    imagen = Column(String)
    copiasPrestadas = Column(Integer)
    descripcion = Column(String)

class Prestamos(Base):
    __tablename__ = 'prestamos'
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id')) 
    libros_id = Column(Integer, ForeignKey('libros.id'))
    fechaprestamos = Column(String) 
    devuelto = Column(Boolean)
