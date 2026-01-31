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
            INSERT INTO libros (`id`, `titulo`, `copias`, `imagen`, `autor`, `copiasPrestadas`, `descripcion`) VALUES
            (1, 'La Biblia', 10, 'biblia.png', 'Varios autores', 1,
            'Texto sagrado compuesto por el Antiguo y el Nuevo Testamento. Recopila relatos históricos, leyes, profecías, poesía y enseñanzas morales que han influido profundamente en la cultura, la ética y la historia de la humanidad durante siglos.'),

            (5, 'Clean Code', 8, 'cleancode.png', 'Robert C. Martin', 0,
            'Guía esencial para programadores que desean escribir código limpio, legible y mantenible. El autor presenta principios, patrones y buenas prácticas para mejorar la calidad del software y facilitar su evolución a largo plazo.'),

            (6, 'Breve historia del tiempo', 5, 'tiempo.png', 'Stephen Hawking', 0,
            'Obra de divulgación científica que explora los grandes misterios del universo: el origen del cosmos, los agujeros negros, la naturaleza del tiempo y las leyes fundamentales de la física, explicadas de forma accesible para el público general.'),

            (7, 'Harry Potter y la piedra filosofal', 10, 'hp1.png', 'J.K. Rowling', 0,
            'Primera entrega de la famosa saga fantástica. Narra la historia de un joven mago que descubre su verdadero origen y comienza su formación en Hogwarts, iniciando una aventura llena de magia, amistad y peligros ocultos.'),

            (8, 'PHP y MySQL', 7, 'phpmysql.png', 'Jon Duckett', 0,
            'Manual práctico y visual para aprender a crear aplicaciones web dinámicas utilizando PHP y bases de datos MySQL. Ideal para principiantes y desarrolladores que quieren construir proyectos reales desde cero.'),

            (9, 'El señor de los anillos', 6, 'lotr.png', 'J.R.R. Tolkien', 1,
            'Épica obra de fantasía ambientada en la Tierra Media. Sigue la misión de destruir un anillo de poder capaz de dominar el mundo, explorando temas como la amistad, el sacrificio y la lucha entre el bien y el mal.'),

            (10, 'El hobbit', 8, 'hobbit.png', 'J.R.R. Tolkien', 0,
            'Precuela de El Señor de los Anillos. Relata el viaje de Bilbo Bolsón, un hobbit corriente que se ve envuelto en una aventura extraordinaria con enanos y un mago, enfrentándose a dragones y criaturas legendarias.'),

            (11, '1984', 9, '1984.png', 'George Orwell', 2,
            'Novela distópica que presenta una sociedad controlada por un régimen totalitario. A través de la vigilancia constante y la manipulación de la información, el autor reflexiona sobre la libertad, el poder y la pérdida de la identidad individual.')
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