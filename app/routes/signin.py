from flask import Blueprint, render_template, request, redirect, url_for, flash, session as flask_session

signin_bp = Blueprint('signin', __name__, template_folder="../../templates")

@signin_bp.route("/signin", methods=["GET", "POST"])
def signin():
    if flask_session.get("usuario_id") or flask_session.get("nombre"):
        return redirect(url_for("libros.ver_libros"))
    
    email = request.form.get("email")
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    password = request.form.get("password")
    direccion = request.form.get("direccion")
    return redirect(url_for("login.login"))