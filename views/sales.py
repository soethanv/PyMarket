from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required


bp = Blueprint('sales', __name__, template_folder='templates', static_folder='static')


@bp.route('/sales')
@login_required
def sales():
    return render_template('sales.html', title='Sales Orders')
