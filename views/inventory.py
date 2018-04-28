from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from models.crud_operations import read_all_products, read_product_batches
from datetime import datetime
import json
from flask import jsonify

bp = Blueprint('inventory', __name__, template_folder='templates', static_folder='static')
sku = None

@bp.route('/inventory', methods=['GET'])
@login_required
def inventory():
    inventory = get_inventory()
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

@bp.route('/getsku', methods=['POST'])
def get_sku():
    global sku
    sku = request.form['row_sku']
    print("Changing sku to "+sku)
    return jsonify(status="success")

def get_inventory():
    inventory = []
    for product in read_all_products():
        inventory.append((product.SKU, product.name, product.category, str(product.price), product.reorder_point, product.stock_quantity, product.storage_location))
    return inventory

def get_batches_with():
    global sku
    print("Called get_batches_with sku "+str(sku))
    batch = read_product_batches(sku)
    print(batch)
    return batch

def check_expiration_date(batch_expiration):
    now = datetime.utcnow()
    diff = batch_expiration - now 
    if diff.days <= 7:
        return True
    else: 
        return False