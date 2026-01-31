from flask import Blueprint, render_template, redirect, url_for, session as flask_session, flash
from app.models.operaciones import Operaciones
from app.models.tablas import Usuarios

admin_bp = Blueprint("admin", __name__, template_folder="../../../templates")

@admin_bp.route("/admin")
def adminpanel():
    if not flask_session.get("usuario_id"):
        return redirect(url_for("login.login"))

    op = Operaciones()
    usuarios = op.mostrarUsu()
    reservas = op.mostrarReservas()

    return render_template("admin/adminpanel.html", usuarios=usuarios, reservas=reservas)


@admin_bp.route("/admin/devolver/<int:id_reserva>")
def devolver_reserva(id_reserva):
    op = Operaciones()
    if op.devolverReserva(id_reserva):
        flash("Reserva devuelta correctamente", "success")
    else:
        flash("No se pudo devolver la reserva", "error")

    return redirect(url_for("admin.adminpanel_bp"))


@admin_bp.route("/admin/borrar_usuario/<int:id_usuario>")
def borrar_usuario(id_usuario):
    op = Operaciones()
    if op.borrarUsuario(id_usuario):
        flash("Usuario eliminado", "success")
    else:
        flash("No se pudo borrar el usuario", "error")

    return redirect(url_for("admin.adminpanel_bp"))
