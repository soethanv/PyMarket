from setup import db
from sqlalchemy import text
from datetime import datetime, date
from models.product import Product
from models.productbatch import ProductBatch
from models.purchaseorder import PurchaseOrder
from models.incomingtransaction import IncomingTransaction
from models.outgoingtransaction import OutgoingTransaction


# Product crud methods

def create_product(SKU, name, category, price, reorder_point, storage_location):
    product = Product(SKU, name, category, price, reorder_point, storage_location)
    try:
        db.session.add(product)
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        raise err


def read_single_product(SKU):
    return Product.query.filter_by(SKU=SKU).first()


def read_all_products():
    return Product.query.all()


def update_product_name(SKU, name):
    try:
        product = Product.query.filter_by(SKU=SKU).first()
        product.name = name
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        raise err


def update_product_reorder_point(SKU, reorder_point):
    try:
        product = Product.query.filter_by(SKU=SKU).first()
        product.reorder_point = reorder_point
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        raise err


def update_product_price(SKU, price):
    try:
        product = Product.query.filter_by(SKU=SKU).first()
        product.price = price
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        raise err


def delete_product(SKU):
    try:
        product = Product.query.filter_by(SKU=SKU).first()

        if product is None:
            raise Exception('Product with ' + str(SKU) + ' does not exist')

        for batch in product.batches:
            db.session.delete(batch)

        db.session.delete(product)
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        raise err


def get_reorder_items():
    return Product.query.filter(Product.stock_quantity <= Product.reorder_point).all()


# Batch crud methods

def create_product_batch(SKU, producer, batch_quantity, year, month, day):
    product_batch = ProductBatch(SKU, producer, batch_quantity, date(year, month, day))
    try:
        db.session.add(product_batch)
        db.session.commit()

        # TODO: make sure product_batch has an ID at this point, verify this gets logged in db
        db.session.add(IncomingTransaction(product_batch.batchID, SKU, producer))

        product = Product.query.filter_by(SKU=SKU).first()
        product.stock_quantity = product.stock_quantity + batch_quantity
        # product.update_stock_quantity()
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        raise err


def read_product_batches(SKU):
    product = Product.query.filter_by(SKU=SKU).first()
    if product is None:
        return None

    return product.batches


def read_single_batch(batchID):
    return ProductBatch.query.filter_by(batchID=batchID).first()


def delete_single_batch(batchID):
    try:
        product_batch = ProductBatch.query.filter_by(batchID=batchID).first()
        product = product_batch.product
        product.stock_quantity = product.stock_quantity - product_batch.batch_quantity
        db.session.delete(product_batch)
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        raise err


def extract_quantity_from_batch(customerID, SKU, requested_quantity):
    '''
        Method doesn't actually return items from the batch,
        but just decrements the requested_quantity from the
        inventory's quantity. Exception is thrown if the
        requested amount is greated than the stock_quantity
    '''
    product = Product.query.filter_by(SKU=SKU).first()

    if product is None:
        raise Exception('Product with ' + str(SKU) + ' does not exist')

    if product.stock_quantity < requested_quantity:
        raise Exception('Not enough stock_quantity to fill order!')

    product.stock_quantity = product.stock_quantity - requested_quantity
    db.session.commit()

    batches = product.batches
    batches = sorted(batches, key=lambda x: x.batch_expiration)

    from_batches_str = ''

    for batch in batches:
        if requested_quantity == 0:
            break

        if batch.batch_quantity <= requested_quantity:
            # batch is too small or just the right amount
            requested_quantity -= batch.batch_quantity
            from_batches_str += (' ' + str(batch.batchID))
            db.session.delete(batch)
        else:
            # batch has more than the requested_quantity
            batch.batch_quantity -= requested_quantity
            from_batches_str += (' ' + str(batch.batchID))
            break

    db.session.commit()

    out_transaction = OutgoingTransaction(customerID, SKU, requested_quantity, from_batches_str)
    db.session.add(out_transaction)
    db.session.commit()


def get_expiring_batches():
    now = datetime.utcnow()

    batches = ProductBatch.query.all()

    if batches is None:
        return None

    expiring_batches = []
    for bt in batches:
        diff = bt.batch_expiration - now

        if diff.days <= 7:
            expiring_batches.append(bt)

    return expiring_batches



# Order crud methods

def read_all_orders():
    return PurchaseOrder.query.filter_by(status='UNFILLED').all()


def update_order_status(poID, new_status):
    try:
        order = PurchaseOrder.query.filter_by(status='UNFILLED').first()
        order.status = new_status
        order.lastUpdatedDt = datetime.utcnow()
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        raise err


def get_order_items(poID):
    query = ('SELECT p.SKU, p.name, p.storage_location, ci.quantity, ci.status, ci.cartItemID, po.customerID '
             'FROM CartItem ci, Product p, PurchaseOrder po '
             'WHERE po.poID = ' + str(poID) + ' and po.cartID = ci.cartID and ci.SKU = p.SKU'
            )

    try:
        query = text(query)
        results = db.engine.execute(query).fetchall()
    except Exception as err:
        db.session.rollback()
        raise err

    return results


def update_order_item_status(cartItemID):
    try:
        cart_item = CartItem.query.filter_by(cartItemID=cartItemID).first()
        cart_item.status = 'FILLED'
        db.session.commit()
    except Exception as err:
        db.session.rollback()
        raise err



# Transaction crud_operations

def get_all_incoming_transactions():
    return IncomingTransaction.query.all()


def get_all_outgoing_transactions():
    return OutgoingTransaction.query.all()
