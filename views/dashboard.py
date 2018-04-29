from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from models.crud_operations import get_expiring_batches, get_reorder_items


bp = Blueprint('dashboard', __name__, template_folder='templates', static_folder='static')


@bp.route('/dashboard')
@login_required
def dashboard():
    items_expiring = []
    for item in get_expiring_batches():
        items_expiring.append((item.batchID, item.SKU, item.product.name
                               , item.batch_quantity, str(item.batch_expiration.date())))

    reorder_items = []
    for item in get_reorder_items():
        reorder_items.append((item.SKU, item.name
                               , item.stock_quantity, item.reorder_point))

    return render_template('dashboard.html', title='Dashboard', expiring=items_expiring, reorder=reorder_items)
