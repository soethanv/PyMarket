from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from models.crud_operations import read_all_orders, get_order_items, update_order_status
from datetime import datetime
from flask import request

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
	hold = []
	inv_dict = {}
	count = 0
	for allproduct in salesparm:
		count += 1
		poID = allproduct[0]
		hold = get_order_items(poID)
		inv_dict[poID] = hold
		for oneproduct in hold:
			inventory.append(list(oneproduct))
		
			
	print(inv_dict[1])
	print(inv_dict)
	
	#inventory.append([344, 'Barley', 'Grain', 1000, 3000])
	#inventory.append([424, 'Apple', 'Fruit', 100, 200])
	return inventory;


#def filled():
	#update_order_status()


