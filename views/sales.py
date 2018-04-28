from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required


bp = Blueprint('sales', __name__, template_folder='templates', static_folder='static')

NumRows = 0

@bp.route('/sales')
@login_required
def sales():
    sales = get_sales()
    salesLen = len(sales)
    inventory = get_inventory()
    return render_template('sales.html', title='Sales Orders', sales=sales, inventory=inventory)


def get_sales():
	sales = []
	sales.append(('1111', 'Carter',  'Food', 'NQ324'))
	sales.append(('2111', 'Gus',  'Food', 'LQ324'))
	sales.append(('3111', 'Dalton',  'Food', 'TQ324'))
	sales.append(('4111', 'Julia',  'Food', 'ZQ324'))
	sales.append(('5111', 'Soe',  'Food', 'WQ324'))
	return sales

def get_inventory():
	inventory = []
	inventory.append([123, 'Cabbage', 'Vegetables', 200, 233])
	inventory.append([421, 'Wheat', 'Grain', 1000, 3000])
	inventory.append([344, 'Barley', 'Grain', 1000, 3000])
	inventory.append([424, 'Apple', 'Fruit', 100, 200])
	return inventory


#def filled():



