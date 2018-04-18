from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user


bp = Blueprint('sales', __name__, template_folder='templates', static_folder='static')


@bp.route('/sales')
def sales():
    if not current_user.is_authenticated:
        return redirect(url_for('login.login'))
    sales = get_sales()
    return render_template('sales.html', title='Sales Orders', sales=sales)


def get_sales():
	sales = []
	sales.append((1111, 'Carter',  'Food', 'NQ324'))
	sales.append((2111, 'Gus',  'Food', 'LQ324'))
	sales.append((3111, 'Dalton',  'Food', 'TQ324'))
	sales.append((4111, 'Julia',  'Food', 'ZQ324'))
	sales.append((5111, 'Soe',  'Food', 'WQ324'))
	return sales