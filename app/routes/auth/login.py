# app/routes/iniciarSesion.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session as flask_session
from app.models.operaciones import Operaciones

iniciarSesion_bp = Blueprint('login', __name__, template_folder="../../../templates")

@iniciarSesion_bp.route("/", methods=["GET", "POST"])
def login():
    if flask_session.get("usuario_id") or flask_session.get("nombre"):
        return redirect(url_for("libros.ver_libros"))
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        usuario = Operaciones.buscarUsuario(email)
        if usuario and usuario.password == password:
            flask_session["usuario_id"] = usuario.id
            flask_session["nombre"] = usuario.nombre
            flask_session["admin"] = usuario.admin
            
            return redirect(url_for("libros.ver_libros"))
        else:
            flash("Credenciales incorrectas", "error")

    return render_template("login/login.html")
