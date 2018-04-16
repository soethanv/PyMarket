from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user


bp = Blueprint('inventory', __name__, template_folder='templates', static_folder='static')


@bp.route('/inventory')
def inventory():
    if not current_user.is_authenticated:
        return redirect(url_for('login.login'))

    return render_template('inventory.html', title='Inventory')
