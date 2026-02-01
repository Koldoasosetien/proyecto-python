from flask import Blueprint, render_template, redirect, url_for, send_file, session as flask_session, flash
from app.models.operaciones import Operaciones
from app.models.tablas import Usuarios
import csv

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

    return redirect(url_for("admin.adminpanel"))


@admin_bp.route("/admin/borrar_usuario/<int:id_usuario>")
def borrar_usuario(id_usuario):
    op = Operaciones()
    if op.borrarUsuario(id_usuario):
        flash("Usuario eliminado", "success")
    else:
        flash("No se pudo borrar el usuario", "error")

    return redirect(url_for("admin.adminpanel"))


@admin_bp.route("/admincsv")
def mostrarCsv():
    reservas = Operaciones.mostrarReservas()
    return render_template("admin/crearcsv.html",reservas=reservas)


@admin_bp.route("/creaRadmincsv")
def CrearCsv():
    reservas = Operaciones.mostrarReservas()
    if reservas:
        with open("reservas.csv", "w", newline='', encoding="utf-8") as f:
            campos = ["ID", "Usuario ID", "Libro ID", "Fecha Prestamo", "Devuelto"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            for r in reservas:
                escritor.writerow({"ID": r.id,"Usuario ID": r.usuario_id, "Libro ID": r.libros_id,"Fecha Prestamo": r.fechaprestamos,"Devuelto": r.devuelto})
        flash("CSV Creado", "msg")
    else:
        flash("CSV no creado, No hay suficiente informacion", "msg")
    return redirect(url_for("admin.adminpanel"))

@admin_bp.route("/admin/descargarCsv")
def descargarCsv():
    return send_file(
        "../reservas.csv",
        as_attachment=True,
        download_name="reservas.csv"
    )
