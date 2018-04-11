from flask import Blueprint, redirect, url_for
from flask_login import logout_user

bp = Blueprint('logout', __name__, template_folder='templates', static_folder='static')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login.login'))
