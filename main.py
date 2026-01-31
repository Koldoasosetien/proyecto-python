# Main.py

# Importar la logica de la aplicacion
from app.app import create_app

# Inicio de la aplicacion
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)