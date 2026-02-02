from flask import Blueprint, render_template, session as flask_session, redirect, url_for
from app.models.operaciones import Operaciones

libros_bp = Blueprint('libros', __name__, template_folder="../../../templates")

@libros_bp.route("/libros", methods=["GET"])
def ver_libros():
    """
        Muestra la lista de libros disponibles para el usuario autenticado.

        Comprueba que el usuario haya iniciado sesión verificando la existencia
        del ID de usuario y el nombre en la sesión. Si no está autenticado,
        se redirige a la página de inicio de sesión.

        Obtiene la lista de libros desde la capa de operaciones y la envía
        a la plantilla principal para su visualización.

        Returns:
            Response: Renderiza la plantilla 'home/home.html' con la lista de libros
            o redirige al login si el usuario no está autenticado.
    """
    
    if not flask_session.get("usuario_id") or not flask_session.get("nombre"):
        return redirect(url_for("login.login"))


    op = Operaciones()
    lista_libros = op.mostrarLibro() 
    
    return render_template("home/home.html", lista_libros=lista_libros)