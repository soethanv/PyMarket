from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required


bp = Blueprint('inventory', __name__, template_folder='templates', static_folder='static')


@bp.route('/inventory')
@login_required
def inventory():
    inventory = get_inventory()
    return render_template('inventory.html', title='Inventory', inventory=inventory)

def get_inventory():
    inventory = []
    inventory.append((123, 'Cabbage', 'Vegetables', 200, 233))
    inventory.append((456, 'Wheat', 'Grain', 1000, 3000))
    inventory.append((789, 'Barley', 'Grain', 1000, 3000))
    inventory.append((567, 'Apple', 'Fruit', 100, 200))
    inventory.append((345, 'Grapes', 'Fruit', 150, 100))
    inventory.append((678, 'Pineapple', 'Fruit', 200, 60))
    inventory.append((921, 'Blueberries', 'Fruit', 140, 80))
    inventory.append((234, 'Blackberries', 'Fruit', 120, 30))
    return inventory
