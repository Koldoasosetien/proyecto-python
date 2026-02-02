from flask import Blueprint, redirect, url_for, flash, session, request ,render_template
from app.models.operaciones import Operaciones

reservas_bp = Blueprint('reservas', __name__, template_folder="../../../templates")

@reservas_bp.route("/reservas", methods=["GET"])
def reservar():
    """
    Realiza la reserva de un libro para el usuario autenticado.

    Obtiene el ID del libro desde los parámetros de la URL y el ID del usuario
    desde la sesión. Si el usuario no ha iniciado sesión o no se especifica
    ningún libro, se redirige con un mensaje de error.

    En caso de que el libro ya esté reservado por el usuario, se muestra un
    mensaje de error. Si la reserva se realiza correctamente, se muestra un
    mensaje de éxito.

    Returns:
        Response: Redirección a la vista de libros tras intentar la reserva.
    """
    
    id_libro = request.args.get('id')
    
    id_usuario = session.get('usuario_id')

    if not id_usuario:
        flash("Debes iniciar sesion para reservar.", "error")
        return redirect(url_for('login.login'))
    
    if not id_libro:
        flash("Error: No se ha especificado ningún libro.", "error")
        return redirect(url_for('home.homePage'))


    op = Operaciones()
    exito = op.realizarReserva(id_libro, id_usuario) 
    if exito == False:
        flash('Ya tienes este libro reservado', 'error')
    else:
        flash('Reserva realizada con exita.', 'success')

    return redirect(url_for("libros.ver_libros"))


@reservas_bp.route("/verReservas", methods=["GET"])
def ver_reservas():
    """
        Muestra todas las reservas realizadas por el usuario autenticado.

        Obtiene el ID del usuario desde la sesión y consulta las reservas asociadas
        a dicho usuario mediante la clase Operaciones.

        Returns:
            Response: Renderiza la plantilla 'verReservas.html' con las reservas
            del usuario.
    """
    
    op = Operaciones()
    idUsu=op.mostrarReservasUsu(session.get('usuario_id'))
    return render_template("verReservas.html",reservasUsu=idUsu)
    