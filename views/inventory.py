from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required


bp = Blueprint('inventory', __name__, template_folder='templates', static_folder='static')


@bp.route('/inventory')
@login_required
def inventory():
    return render_template('inventory.html', title='Inventory')
