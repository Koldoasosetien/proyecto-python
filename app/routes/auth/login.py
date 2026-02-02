# app/routes/iniciarSesion.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session as flask_session
from app.models.operaciones import Operaciones

iniciarSesion_bp = Blueprint('login', __name__, template_folder="../../../templates")

@iniciarSesion_bp.route("/", methods=["GET", "POST"])
def login():
    """
        Gestiona el inicio de sesión de los usuarios.

        - Si el usuario ya tiene una sesión activa, se redirige directamente
        a la vista principal de libros.
        - En una petición POST, valida las credenciales introducidas por el
        usuario comparándolas con las almacenadas en el sistema.
        - Si las credenciales son correctas, se guardan los datos básicos del
        usuario en la sesión.
        - Si son incorrectas, se muestra un mensaje de error.

        Returns:
            Response: Renderiza la plantilla de login o redirige a la vista de
            libros si el inicio de sesión es exitoso.
    """
    
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
