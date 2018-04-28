from flask import Blueprint, render_template
from flask_login import login_required
from models.crud_operations import get_all_incoming_transactions, get_all_outgoing_transactions

bp = Blueprint('transaction', __name__, template_folder='templates', static_folder='static')


@bp.route('/intransaction', methods=['GET'])
@login_required
def incoming_transactions():
    transactions = []
    for tr in get_all_incoming_transactions():
        transactions.append((tr.batchID, tr.SKU, tr.producer, tr.transactionDate))
    return render_template('transaction.html', title='Incoming Transactions', transactions=transactions, display='INCOMING')



@bp.route('/outtransaction', methods=['GET'])
@login_required
def outgoing_transactions():
    transactions = []
    for tr in get_all_outgoing_transactions():
        transactions.append((tr.outTransactionID, tr.customerID, tr.SKU, tr.quantity, tr.from_batches, tr.transactionDate))
    return render_template('transaction.html', title='Outgoing Transactions', transactions=transactions, display='OUTGOING')


# @bp.route('/outtransaction', methods=['GET'])
# @login_required
# def inventory():
#     transactions = get_all_incoming_transactions()
#     inventory = get_inventory()
#     get_batches_with(90821)
#     return render_template('intransaction.html', title='Incoming Transactions', inventory=inventory, get_batches_with=get_batches_with, check_expiration_date=check_expiration_date)
