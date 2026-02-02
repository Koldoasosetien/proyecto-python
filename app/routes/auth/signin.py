from flask import Blueprint, render_template, request, redirect, url_for, flash, session as flask_session
from app.models.operaciones import Operaciones

signin_bp = Blueprint('signin', __name__, template_folder="../../../templates")

@signin_bp.route("/signin", methods=["GET", "POST"])
def signin():
    """
        Gestiona el registro de nuevos usuarios.

        - Si el usuario ya ha iniciado sesión, se redirige a la vista principal
        de libros.
        - En una petición POST, valida los datos introducidos en el formulario
        de registro.
        - Comprueba si el correo electrónico ya está registrado en el sistema.
        - Si no existe, crea un nuevo usuario y muestra un mensaje de éxito.
        - En caso de error, muestra el mensaje correspondiente.

        Returns:
            Response: Renderiza la plantilla de registro o redirige al login
            tras un registro exitoso.
    """
    
    # Si ya está logueado
    if flask_session.get("usuario_id") or flask_session.get("nombre"):
        return redirect(url_for("libros.ver_libros"))

    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellidos = request.form.get("apellidos")
        email = request.form.get("email")
        password = request.form.get("password")

        if not nombre or not apellidos or not email or not password:
            flash("Todos los campos son obligatorios", "error")
            return redirect(url_for("signin.signin"))

        op = Operaciones()

        # Comprobar si el usuario ya existe
        usuario_existente = op.buscarUsuario(email)
        if usuario_existente:
            flash("Ese email ya está registrado", "error")
            return redirect(url_for("signin.signin"))

        # Crear usuario
        creado = op.crear_usuario(nombre, email, password, apellidos)
        if creado:
            flash("Usuario creado correctamente. Inicia sesión.", "success")
            return redirect(url_for("login.login"))
        else:
            flash("Error al crear el usuario", "error")

    return render_template("signin/signin.html")
