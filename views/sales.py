from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from models.crud_operations import read_all_orders, get_order_items, update_order_status
from datetime import datetime
from flask import request
import json
from flask import jsonify

bp = Blueprint('sales', __name__, template_folder='templates', static_folder='static')

poID = None

@bp.route('/sales')
@login_required
def sales():
    sales = get_orders()
    salesLen = len(sales)
    #inventory = get_inventory(sales)
    return render_template('sales.html', title='Sales Orders', sales=sales)

def get_orders():
	order = []
	for sales in read_all_orders():
		order.append((sales.poID, sales.customerID, sales.createdDt, sales.status))

	return order


@bp.route('/getproductdata', methods=["GET", "POST"])
def get_inventory():
	poID = request.form['row_OrderId']
	print("Product Data before printing")
	product_data = get_products_with(poID)
	print(product_data)
	return jsonify(status="success", data=product_data)



def get_products_with(podID):
	if podID is None:
		podID = 1
	print("Called get_products_with poId " + str(podID))
	product = get_order_items(podID)
	products = []
	for prod in product:
		products.append((prod[0], prod[1], prod[2], prod[3]))
	return products	


@bp.route('/fillproductdata', methods=["GET", "POST"])
def filled():
	SKU = request.form['row_SKU']
	quantity = request.form['row_quantity']
	print("\n\nTaking out "+ quantity)
	print(" for SKU " + SKU)
	print("\n\n")
	
	
	


