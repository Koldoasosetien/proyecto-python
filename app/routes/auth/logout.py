from flask import Blueprint, render_template, request, redirect, url_for, flash, session as flask_session

logout_bp = Blueprint('logout', __name__, template_folder="../../../templates")

@logout_bp.route("/logout", methods=["GET", "POST"])
def logout():
    flask_session.clear()
    
    return redirect(url_for("login.login"))