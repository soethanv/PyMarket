from setup import db
from sqlalchemy import text
from datetime import datetime
from models.product import Product
from models.productbatch import ProductBatch
from models.purchaseorder import PurchaseOrder

# TODO: make exception handling less generic


# Product crud methods

def create_product(SKU, name, category, price, reorder_point, stock_quantity):
    product = Product(SKU, name, category, price, reorder_point, stock_quantity)
    try:
        db.session.add(product)
        db.session.commit()
    except Exception as err:
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
        raise err


def update_product_reorder_point(SKU, reorder_point):
    try:
        product = Product.query.filter_by(SKU=SKU).first()
        product.reorder_point = reorder_point
        db.session.commit()
    except Exception as err:
        raise err


def update_product_price(SKU, price):
    try:
        product = Product.query.filter_by(SKU=SKU).first()
        product.price = price
        db.session.commit()
    except Exception as err:
        raise err


def delete_product(SKU):
    try:
        product = Product.query.filter_by(SKU=SKU).first()
        db.session.delete(product)
        db.session.commit()
    except Exception as err:
        raise err



# Batch crud methods

def create_product_batch(SKU, batch_quantity, year, month, day):
    product_batch = ProductBatch(SKU, batch_quantity, date(year, month, day))
    try:
        db.session.add(product_batch)
        db.session.commit()
        product = read_single_product(SKU)
        product.update_stock_quantity()
        db.session.commit()
    except Exception as err:
        raise err


def read_product_batches(SKU):
    product = Product.query.filter_by(SKU=SKU).first()
    return product.batches


def read_single_batch(batchID):
    return ProductBatch.query.filter_by(batchID=batchID).first()


def extract_quantity_from_batch(SKU, requested_quantity):
    '''
        Method doesn't actually return items from the batch,
        but just decrements the requested_quantity from the
        inventory's quantity. Exception is thrown if the
        requested amount is greated than the stock_quantity
    '''
    product = Product.query.filter_by(SKU=SKU).first()

    if product.stock_quantity < requested_quantity:
        raise Exception('Not enough stock_quantity to fill order!')

    product.stock_quantity = product.stock_quantity - requested_quantity
    db.session.commit()

    batches = product.batches
    batches = sorted(batches, key=lambda x: x.batch_expiration)

    for batch in batches:
        if requested_quantity == 0:
            break

        if batch.batch_quantity <= requested_quantity:
            # batch is too small or just the right amount
            requested_quantity -= batch.batch_quantity
            db.session.delete(batch)
        else:
            # batch has more than the requested_quantity
            batch.batch_quantity -= requested_quantity
            break


    db.session.commit()



# Order crud methods

def read_all_orders():
    return PurchaseOrder.query.filter_by(status='UNFILLED').all()


def update_order_status(poID, new_status):
    try:
        order = PurchaseOrder.query.filter_by(status='UNFILLED').first()
        order.status = new_status
        order.lastUpdatedDt = datetime.utcnow
        db.session.commit()
    except Exception as err:
        raise err


def get_order_items(poID):
    query = ('SELECT p.SKU, p.name, p.storage_location, p.price, ci.quantity '
             'FROM CartItem ci, Product p, PurchaseOrder po '
             'WHERE po.poID = ' + str(poID) + ' and po.cartID = ci.cartID and ci.SKU = p.SKU'
            )

    try:
        query = text(query)
        results = db.engine.execute(query).fetchall()
    except Exception as err:
        raise err

    return results
