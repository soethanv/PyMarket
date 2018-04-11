from flask import Blueprint, render_template


bp = Blueprint('dashboard', __name__, template_folder='templates', static_folder='static')


@bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Dashboard')
