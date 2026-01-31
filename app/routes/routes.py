from app.routes.iniciarSesion import iniciarSesion_bp
from app.routes.logout import logout_bp
from app.routes.libros import libros_bp
from app.routes.reserva import reservas_bp
ALL_BLUEPRINTS = (
    iniciarSesion_bp,
    logout_bp,
    libros_bp,
    reservas_bp,
)