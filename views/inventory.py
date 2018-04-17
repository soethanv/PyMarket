from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user


bp = Blueprint('inventory', __name__, template_folder='templates', static_folder='static')


@bp.route('/inventory')
def inventory():
    if not current_user.is_authenticated:
        return redirect(url_for('login.login'))
    inventory = get_inventory()
    return render_template('inventory.html', title='Inventory', inventory=inventory)

def get_inventory():
    inventory = []
    inventory.append((123, 'Cabbage', 'Vegetables', 200, 233))
    inventory.append((456, 'Wheat', 'Grain', 1000, 3000))
    inventory.append((456, 'Barley', 'Grain', 1000, 3000))
    inventory.append((456, 'Apple', 'Fruit', 100, 200))
    return inventory
