from app.routes.auth.login import iniciarSesion_bp
from app.routes.auth.logout import logout_bp
from app.routes.auth.signin import signin_bp
from app.routes.user.libros import libros_bp
from app.routes.user.reserva import reservas_bp
from app.routes.admin.adminpanel import admin_bp
ALL_BLUEPRINTS = (
    iniciarSesion_bp,
    logout_bp,
    libros_bp,
    reservas_bp,
    signin_bp,
    admin_bp,
)
