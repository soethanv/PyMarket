from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from models.crud_operations import create_product

bp = Blueprint('inventory', __name__, template_folder='templates', static_folder='static')


@bp.route('/inventory', methods=['GET'])
@login_required
def inventory():
    inventory = get_inventory()
    return render_template('inventory.html', title='Inventory', inventory=inventory)

@bp.route('/inventoryadder', methods=['POST'])
def handle_add():
    print("I am adding an product")

    SKU = request.form['SKU']
    name = request.form['Name']
    reorder_point = request.form['RP']
    quantity = request.form['Amount']
    price = request.form['Price']
    category = request.form['Cat']
    stock = request.form['Stock']
    create_product(SKU, name, category, price, reorder_point, stock)
    return redirect('/inventory', code=302)

@bp.route('/inventoryediter', methods=['POST'])
def handle_edit():
    print("I am editing a product")
    return redirect('/inventory', code=302)

def get_inventory():
    inventory = []
    inventory.append((123, 'Cabbage', 200, 233))
    inventory.append((456, 'Wheat', 1000, 3000))
    inventory.append((456, 'Barley', 1000, 3000))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    inventory.append((456, 'Apple', 100, 200))
    return inventory
