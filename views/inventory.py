from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_login import login_required
from models.crud_operations import read_all_products, read_product_batches, read_single_product, \
create_product, update_product_name, update_product_reorder_point, update_product_price, delete_product, \
delete_single_batch, create_product_batch
from datetime import datetime
import json
from flask import jsonify

bp = Blueprint('inventory', __name__, template_folder='templates', static_folder='static')
sku = None

@bp.route('/inventory', methods=['GET'])
@login_required
def inventory():
    inventory = get_inventory()
    print("jsonify")
    return render_template('inventory.html', title='Inventory', inventory=inventory, check_expiration_date=check_expiration_date)

@bp.route('/inventoryadder', methods=['POST'])
def handle_add_product():
    print('I am adding a product')
    SKU = request.form['SKU']
    name = request.form['Name']
    reorder_point = request.form['RP']
    price = request.form['Price']
    category = request.form['Category']
    storage_location = request.form['Location']
    create_product(SKU, name, category, price, reorder_point, storage_location)
    return redirect('/inventory', code=302)

@bp.route('/batchesadd', methods=['POST'])
def handle_add_batch():
    print('I am adding a batch')
    SKU = request.form['batchSKU']
    producer = request.form['Producer']
    stock = request.form['Quantity']
    day = request.form['Day']
    month = request.form['Month']
    year = request.form['Year']
    print(SKU+' '+producer+' '+stock+' '+day+' '+month+' '+year)
    create_product_batch(SKU, producer, int(stock), int(year), int(month), int(day))
    return redirect('/inventory', code=302)

@bp.route('/inventoryeditor', methods=['POST'])
def handle_edit():
    print('I am editing a product')
    SKU = request.form['SKU']
    # Compare with database
    product = read_single_product(SKU)
    print(product)
    name = request.form['Name']
    if product.name != name:
        update_product_name(SKU, name)
    reorder_point = request.form['RP']
    if product.reorder_point != reorder_point:
        update_product_reorder_point(SKU, reorder_point)
    price = request.form['Price']
    if product.price != price:
        update_product_price(SKU, price)
    return redirect('/inventory', code=302)



@bp.route('/inventorydelete', methods=['POST'])
def handle_delete_product():
    print('I am deleting a product')
    SKU = request.form['row_sku']
    print(SKU)
    delete_product(SKU)
    return jsonify(status='success')

@bp.route('/batchesdelete', methods=['POST'])
def handle_delete_batch():
    print('I am deleting a batch')
    batchID= request.form['row_id']
    #print(batchID)
    delete_single_batch(batchID)
    return jsonify(status='success')


def get_inventory():
    inventory = []
    for product in read_all_products():
        inventory.append((product.SKU, product.name, product.category, str(product.price), product.reorder_point, product.stock_quantity, product.storage_location))
    return inventory

@bp.route('/getbatchdata', methods=["GET", "POST"])
def get_sku():
    sku = request.form['row_sku']
    #print("batch data before printing")
    batch_data = get_batches_with(sku)
    print(batch_data)
    return jsonify(status="success", data=batch_data)

def get_batches_with(SKU):
    # need to handle this more efficiently
    if SKU is None:
        SKU = 1234
    #print("Called get_batches_with SKU " + str(SKU))
    batch = read_product_batches(SKU)
    batches = []
    for bat in batch:
        batches.append((bat.batchID, bat.producer, bat.batch_quantity, bat.batch_expiration))
    return batches

def check_expiration_date(batch_expiration):
    now = datetime.utcnow()
    diff = batch_expiration - now
    if diff.days <= 7:
        return True
    else:
        return False
