from flask import Blueprint, render_template, session as flask_session, redirect, url_for
from app.models.operaciones import Operaciones

libros_bp = Blueprint('libros', __name__, template_folder="../../../templates")

@libros_bp.route("/libros", methods=["GET"])
def ver_libros():

    if not flask_session.get("usuario_id") or not flask_session.get("nombre"):
        return redirect(url_for("login.login"))


    op = Operaciones()
    lista_libros = op.mostrarLibro() 
    
    return render_template("home/home.html", lista_libros=lista_libros)