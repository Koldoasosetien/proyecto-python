# app/models/operaciones.py

from app.models.tablas import Usuarios, Libro, Prestamos
from app.models.db import session
from datetime import date

class Operaciones:

    # Cosas
    def crear_usuario(self, nombre, email, password,apellidos):
        nuevoUsu= Usuarios(nombre=nombre, email=email, password=password, admin=False,apellidos=apellidos)
        try:
            session.add(nuevoUsu)
            session.commit()
            print("Usuario creado con exito")
            return True
        except Exception as e:
            print("algo ha fallado")
            session.rollback()
            return False
        

    def eliminar_usuario(self,usuario_Id):
        usuario=session.query(Usuarios).filter_by(Usuarios.id==usuario_Id).first()
        try:
            if(usuario):
                session.delete(usuario)
                session.commit()
                print("Usuario eliminado")
            else:
                print("Usuario no encontrado")
        except Exception as e:
            print("algo  ha fallado")
            session.rollback()
            return False
        

    def modificar_usuario(self,id_usuario,nombre, apellidos, email, password, direccion):

        try:
            session.query(Usuarios).filter_by(Usuarios.id==id_usuario).update({"nombre":nombre, "apellidos":apellidos, "email":email,"password":password, "direccion":direccion })
            session.commit()
        except Exception as e:
            print("algo  ha fallado")
            session.rollback()
            return False
        
    
    @staticmethod
    def buscarUsuario(email):
        return session.query(Usuarios).filter(Usuarios.email == email) .first()




# Mostrar
    def mostrarUsu(self):
        usuarios=session.query(Usuarios).all()
        print(usuarios)
        return usuarios

    def mostrarLibro(self):
        libros=session.query(Libro).all()
        print(libros)
        return libros



    def realizarReserva(self, id_libro, id_usuario):
        try:

            tieneLibro = session.query(Prestamos).filter(Prestamos.libros_id == id_libro, Prestamos.usuario_id == id_usuario,Prestamos.devuelto == False).first()
            if tieneLibro:
                return False
            
            fecha_hoy = date.today().strftime('%d/%m/%Y') 
            nuevo_prestamo = Prestamos(usuario_id=id_usuario, libros_id=id_libro, fechaprestamos=fecha_hoy, devuelto=False)
            session.add(nuevo_prestamo)
            libro = session.query(Libro).filter(Libro.id == id_libro).first()
            libro.copiasPrestadas += 1 
            session.commit()
            return True

        except Exception as e:
            print("algo  ha fallado")
            session.rollback()
            return False







if __name__=="__main__":
    o=Operaciones()

    # o.mostrarUsu()
