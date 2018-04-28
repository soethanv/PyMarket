from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from models.crud_operations import read_all_orders, get_order_items, update_order_status
from datetime import datetime

bp = Blueprint('sales', __name__, template_folder='templates', static_folder='static')

NumRows = 0

@bp.route('/sales')
@login_required
def sales():
    sales = get_orders()
    salesLen = len(sales)
    inventory = get_inventory(sales)
    return render_template('sales.html', title='Sales Orders', sales=sales, inventory=inventory)

def get_orders():
	order = []
	for sales in read_all_orders():
		order.append((sales.poID, sales.customerID, sales.createdDt, sales.status))

	return order

def get_inventory(salesparm):
	inventory = []
	
	for po in salesparm:
		print(get_order_items(po[0]))
	
	inventory.append([123, 'Cabbage', 'Vegetables', 200, 233])
	inventory.append([421, 'Wheat', 'Grain', 1000, 3000])
	#inventory.append([344, 'Barley', 'Grain', 1000, 3000])
	#inventory.append([424, 'Apple', 'Fruit', 100, 200])
	return inventory


def filled():
	update_order_status()


