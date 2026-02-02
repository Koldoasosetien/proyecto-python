# Biblioteca Flask

## Requisitos

- Python 3.9 o superior  
- pip

Comprobar la versión de Python:

```bash
python --version
```

---

## Instalación

### 1. Clonar o descargar el proyecto

Para clonar:

```bash
git clone https://github.com/Koldoasosetien/proyecto-python.git
```

---

### 2. Crear un entorno virtual (venv)

#### Windows

```bash
python -m venv env
.\env\scripts\activate.ps1
```

#### Linux / macOS

```bash
python3 -m venv env
source env/bin/activate
```

Cuando el entorno esté activo aparecerá:

```text
(env)
```

---

### 3. Instalar dependencias

Con el entorno virtual activo:

```bash
pip install -r requirements.txt
```

---

## Base de datos

La aplicación utiliza **SQLite**, por lo que no es necesario configurar un servidor externo.

El archivo de base de datos se crea automáticamente.  
Alternativamente, se incluye una base de datos prehecha:

```text
biblioteca.db
```

---

## Uso de la aplicación

### 1. Ejecutar la aplicación

Desde la raíz del proyecto:

```bash
python main.py
```

---

### 2. Acceder desde el navegador

```text
http://127.0.0.1:5000
```
