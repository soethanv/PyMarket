from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from models.crud_operations import read_all_orders, get_order_items, update_order_status, extract_quantity_from_batch, update_order_item_status
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
		products.append((prod[0], prod[1], prod[2], prod[3], prod.status, prod.cartItemID, prod.customerID))
	return products	


@bp.route('/fillproductdata', methods=["GET", "POST"])
def filledproductdata():
	SKU = request.form['row_SKU']
	quantity = request.form['row_quantity']
	OrderId = request.form['row_OrderId']
	cartID = request.form['row_cartId']
	print("and cartID" + cartID)
	print("\n\nTaking out "+ quantity)
	print("for SKU " + SKU)
	print("with Order Id " + OrderId)
	print("\n\n")
	extract_quantity_from_batch(int(OrderId), int(SKU), int(quantity))
	update_order_item_status(int(cartID))
	return jsonify(status='success')
	#extract_quantity_from_batch(OrderId, SKU, quantity)


@bp.route('/filledbutton', methods=['POST'])
def handle_filled_order():
    print('Im filling a product')
    OrderId = request.form['row_OrderId']
    print(OrderId)
    return jsonify(status='success')

	


