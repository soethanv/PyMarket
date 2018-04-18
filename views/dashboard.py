from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required


bp = Blueprint('dashboard', __name__, template_folder='templates', static_folder='static')


@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')
