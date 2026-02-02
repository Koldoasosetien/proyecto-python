# app/models/consultas.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Usuarios(Base):
    """
        Modelo que representa a los usuarios del sistema.

        Almacena la información básica de cada usuario, incluyendo
        sus datos personales.
    """

    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellidos = Column(String) 
    email = Column(String)
    password = Column(String)
    direccion = Column(String) 
    admin = Column(Boolean)

class Libro(Base):
    """
        Modelo que representa los libros disponibles en la biblioteca.

        Contiene la información descriptiva de cada libro.
    """
    
    __tablename__ = 'libros'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    autor = Column(String)
    copias = Column(Integer)
    imagen = Column(String)
    copiasPrestadas = Column(Integer)
    descripcion = Column(String)

class Prestamos(Base):
    """
        Modelo que representa los préstamos de libros realizados por los usuarios.

        Relaciona un usuario con un libro y almacena la fecha del préstamo
        junto con el estado de devolución.
    """
    
    __tablename__ = 'prestamos'
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id')) 
    libros_id = Column(Integer, ForeignKey('libros.id'))
    fechaprestamos = Column(String) 
    devuelto = Column(Boolean)
