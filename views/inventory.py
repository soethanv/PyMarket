from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from models.crud_operations import read_all_products, read_product_batches
from datetime import datetime

bp = Blueprint('inventory', __name__, template_folder='templates', static_folder='static')


@bp.route('/inventory', methods=['GET'])
@login_required
def inventory():
    inventory = get_inventory()
    get_batches_with(90821)
    return render_template('inventory.html', title='Inventory', inventory=inventory, get_batches_with=get_batches_with, check_expiration_date=check_expiration_date)

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
    for product in read_all_products():
        inventory.append((product.SKU, product.name, product.category, str(product.price), product.reorder_point, product.stock_quantity, product.storage_location))
    return inventory

def get_batches_with(SKU):
    batch = read_product_batches(SKU)
    print(batch)
    return batch

def check_expiration_date(batch_expiration):
    now = datetime.utcnow()
    # tokens = batch_expiration.split(' ')
    # tokens = tokens[0].split('-')
    # expiration = datetime.date(tokens[0], tokens[1], tokens[2])
    print(type(batch_expiration))
    print(type(now))
    diff = batch_expiration - now 
    if diff.days <= 7:
        return True
    else: 
        return False