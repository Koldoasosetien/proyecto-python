from flask import Blueprint, render_template, redirect, url_for, send_file, session as flask_session, flash
from app.models.operaciones import Operaciones
from app.models.tablas import Usuarios
import csv

admin_bp = Blueprint("admin", __name__, template_folder="../../../templates")

@admin_bp.route("/admin")
def adminpanel():
    """
        Muestra el panel de administración.

        Verifica que el usuario haya iniciado sesión. Si no es así, redirige
        a la página de login. En caso contrario, obtiene la lista de usuarios
        y de reservas para mostrarlas en el panel de administración.

        Returns:
            Response: Renderiza la plantilla 'admin/adminpanel.html' con los
            usuarios y reservas, o redirige al login.
    """
    
    if not flask_session.get("usuario_id"):
        return redirect(url_for("login.login"))

    op = Operaciones()
    usuarios = op.mostrarUsu()
    reservas = op.mostrarReservas()

    return render_template("admin/adminpanel.html", usuarios=usuarios, reservas=reservas)


@admin_bp.route("/admin/devolver/<int:id_reserva>")
def devolver_reserva(id_reserva):
    """
        Marca una reserva como devuelta.

        Recibe el ID de la reserva desde la URL y llama a la capa de operaciones
        para actualizar su estado. Muestra un mensaje informativo según el
        resultado de la operación.

        Args:
            id_reserva (int): Identificador de la reserva a devolver.

        Returns:
            Response: Redirección al panel de administración.
    """
    
    op = Operaciones()
    if op.devolverReserva(id_reserva):
        flash("Reserva devuelta correctamente", "success")
    else:
        flash("No se pudo devolver la reserva", "error")

    return redirect(url_for("admin.adminpanel"))


@admin_bp.route("/admin/borrar_usuario/<int:id_usuario>")
def borrar_usuario(id_usuario):
    """
        Elimina un usuario del sistema.

        Recibe el ID del usuario desde la URL y solicita su eliminación a la
        capa de operaciones. Muestra un mensaje de éxito o error según el
        resultado.

        Args:
            id_usuario (int): Identificador del usuario a eliminar.

        Returns:
            Response: Redirección al panel de administración.
    """
    op = Operaciones()
    if op.borrarUsuario(id_usuario):
        flash("Usuario eliminado", "success")
    else:
        flash("No se pudo borrar el usuario", "error")

    return redirect(url_for("admin.adminpanel"))


@admin_bp.route("/admincsv")
def mostrarCsv():
    """
        Muestra la vista previa de las reservas para la creación del CSV.

        Obtiene todas las reservas del sistema y las envía a la plantilla
        encargada de mostrar la información antes de generar el archivo CSV.

        Returns:
            Response: Renderiza la plantilla 'admin/crearcsv.html' con las reservas.
    """
    
    reservas = Operaciones.mostrarReservas()
    return render_template("admin/crearcsv.html",reservas=reservas)


@admin_bp.route("/creaRadmincsv")
def CrearCsv():
    """
        Genera un archivo CSV con todas las reservas del sistema.

        Obtiene las reservas desde la capa de operaciones y, si existen,
        crea un archivo 'reservas.csv' con la información relevante.
        Muestra un mensaje indicando si el archivo se ha creado correctamente
        o si no había datos suficientes.

        Returns:
            Response: Redirección al panel de administración.
    """

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
    """
        Permite descargar el archivo CSV de reservas.

        Envía el archivo 'reservas.csv' como adjunto para que el administrador
        pueda descargarlo.

        Returns:
            Response: Archivo CSV descargable.
    """
    
    return send_file(
        "../reservas.csv",
        as_attachment=True,
        download_name="reservas.csv"
    )
