from flask import Blueprint, render_template, request, redirect, url_for, flash, session as flask_session

logout_bp = Blueprint('logout', __name__, template_folder="../../../templates")

@logout_bp.route("/logout", methods=["GET", "POST"])
def logout():
    """
        Cierra la sesión del usuario.

        Elimina todos los datos almacenados en la sesión actual, incluyendo
        la información de autenticación, y redirige al usuario a la página
        de inicio de sesión.

        Returns:
            Response: Redirección a la vista de login.
    """
    
    flask_session.clear()
    
    return redirect(url_for("login.login"))