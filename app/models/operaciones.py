# app/models/operaciones.py

from app.models.tablas import Usuarios, Libro, Prestamos
from app.models.db import session
from datetime import date

class Operaciones:

    # Cosas
    @staticmethod
    def crear_usuario(nombre, email, password,apellidos):
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
        

    @staticmethod
    def eliminar_usuario(usuario_Id):
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
        

    @staticmethod
    def modificar_usuario(id_usuario,nombre, apellidos, email, password, direccion):

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
    @staticmethod
    def mostrarUsu():
        usuarios=session.query(Usuarios).all()
        print(usuarios)
        return usuarios

    @staticmethod
    def mostrarLibro():
        libros=session.query(Libro).all()
        print(libros)
        return libros



    @staticmethod
    def realizarReserva(id_libro, id_usuario):
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

    @staticmethod
    def mostrarReservas():
        return session.query(Prestamos).all()
    

    @staticmethod
    def mostrarLibroUsu(idLibro):
        libros=session.query(Libro).filter(Libro.id==idLibro).first()
        print(libros)
        return libros
    
    @staticmethod
    def mostrarReservasUsu(idUsu):
        tieneReservas=session.query(Prestamos).filter(Prestamos.usuario_id==idUsu).all()
        listaLibros=list()
        if tieneReservas:
           for reserva in tieneReservas:
               listaLibros.append(Operaciones.mostrarLibroUsu(reserva.libros_id))
        return listaLibros

  




    @staticmethod
    def devolverReserva(id_reserva):
        try:
            prestamo = session.query(Prestamos).filter(Prestamos.id == id_reserva).first()
            if prestamo and not prestamo.devuelto:
                prestamo.devuelto = True

                libro = session.query(Libro).filter(Libro.id == prestamo.libros_id).first()
                libro.copiasPrestadas -= 1

                session.commit()
                return True
        except Exception as e:
            print ("error")
            session.rollback()
            return False

    @staticmethod
    def borrarUsuario(id_usuario):
        try:
            usuario = session.query(Usuarios).filter(Usuarios.id == id_usuario).first()
            if usuario and not usuario.admin:
                session.delete(usuario)
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            return False


if __name__=="__main__":
    o=Operaciones()

    # o.mostrarUsu()
