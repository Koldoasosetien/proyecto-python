# app/models/tablas.py

import sqlite3

class GestionarBiblioteca:
    def __init__(self, nombre_db="biblioteca.db"):
        self.conexion = sqlite3.connect(nombre_db)
        self.crear_tabla()
       
        
    def crear_tabla(self):
        cursor = self.conexion.cursor()
        cursor.execute("PRAGMA foreign_keys = 1")

        # Tabla libros
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            copias INTEGER,
            imagen TEXT,
            copiasPrestadas INTEGER,
            descripcion TEXT
        )
        ''')

        # Tabla usuarios 
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            apellidos TEXT,
            email TEXT,
            password TEXT,
            direccion TEXT,
            admin BOOLEAN 
        )
        ''')

        # Tabla prestamos
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS prestamos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,              
            libros_id INTEGER,
            fechaprestamos TEXT,              
            devuelto BOOLEAN,        
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
            FOREIGN KEY(libros_id) REFERENCES libros(id)
        )
        ''')
        print("Tablas creadas ")
        self.conexion.commit()

    def inserciones(self):
        cursor = self.conexion.cursor()
        
        cursor.execute('''
            INSERT  INTO libros (`id`, `titulo`, `copias`, `imagen`, `autor`, `copiasPrestadas`, `descripcion`) VALUES
            (1, 'La Biblia', 10, 'biblia.png', '', 1, 'Descripción de la biblia...'),
            (5, 'Clean Code', 8, 'cleancode.png', 'Robert C. Martin', 0, 'Buenas prácticas...'),
            (6, 'Breve historia del tiempo', 5, 'tiempo.png', 'Stephen Hawking', 0, 'Cosmología...'),
            (7, 'Harry Potter', 10, 'hp1.png', 'J.K. Rowling', 0, 'Mago...'),
            (8, 'PHP y MySQL', 7, 'phpmysql.png', 'Jon Duckett', 0, 'Desarrollo web...')
        ''')

        cursor.execute('''
            INSERT  INTO usuarios (`id`, `nombre`, `apellidos`, `email`, `password`, `direccion`, `admin`) VALUES
            (1, 'Administrador', NULL, 'admin@admin.com', '123', NULL, 1),
            (10, 'test', 'test', 'test@test.com', '123', 'test', 0),
            (11, 'Koldo', 'Aso', 'Koldo@gmail.com', '123', '1234', 0),
            (12, 'Ana', 'Martínez', 'ana@correo.com', '123', 'Calle Mayor 12', 0)
        ''')

        print("Inserciones aplicadas correctamente.")
        self.conexion.commit()

if __name__=="__main__":
    b = GestionarBiblioteca()
    b.crear_tabla()
    b.inserciones()