from flask import Blueprint, redirect, url_for, flash, session, request 
from app.models.operaciones import Operaciones

reservas_bp = Blueprint('reservas', __name__, template_folder="../../templates")

@reservas_bp.route("/reservas", methods=["GET"])
def reservar():
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