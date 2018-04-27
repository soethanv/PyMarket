from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required


bp = Blueprint('sales', __name__, template_folder='templates', static_folder='static')

NumRows = 0

@bp.route('/sales')
@login_required
def sales():
    sales = get_sales()
    salesLen = len(sales)
    return render_template('sales.html', title='Sales Orders', sales=sales, salesLen=salesLen, NumRows=NumRows, myFunction=increment)

def increment(numAdded):
	global NumRows
	NumRows += numAdded
	return NumRows


def get_sales():
	sales = []
	inventory = []
	inventory.append([123, 'Cabbage', 'Vegetables', 200, 233])
	inventory.append([456, 'Wheat', 'Grain', 1000, 3000])
	inventory.append([456, 'Barley', 'Grain', 1000, 3000])
	inventory.append([456, 'Apple', 'Fruit', 100, 200])
	sales.append((1111, 'Carter',  'Food', 'NQ324', inventory))
	sales.append((2111, 'Gus',  'Food', 'LQ324', inventory))
	sales.append((3111, 'Dalton',  'Food', 'TQ324', inventory))
	sales.append((4111, 'Julia',  'Food', 'ZQ324', inventory))
	sales.append((5111, 'Soe',  'Food', 'WQ324', inventory))
	return sales
