from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required
from models.crud_operations import get_all_incoming_transactions
from datetime import datetime

bp = Blueprint('intransaction', __name__, template_folder='templates', static_folder='static')


@bp.route('/intransaction', methods=['GET'])
@login_required
def inventory():
    transactions = get_all_incoming_transactions()
    inventory = get_inventory()
    get_batches_with(90821)
    return render_template('intransaction.html', title='Incoming Transactions', inventory=inventory, get_batches_with=get_batches_with, check_expiration_date=check_expiration_date)




def get_incoming_transactions():
    transactions = []
    for product in read_all_products():
        inventory.append((product.SKU, product.name, product.category, str(product.price), product.reorder_point, product.stock_quantity, product.storage_location))
    return inventory
