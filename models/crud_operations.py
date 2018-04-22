from setup import db
from sqlalchemy import text
from datetime import datetime
from models.product import Product
from models.purchaseorder import PurchaseOrder

# TODO: make exception handling less generic



def create_product(SKU, name, category, price, reorder_point, stock_quantity):
    product = Product(SKU, name, category, price, reorder_point, stock_quantity)
    try:
        db.session.add(product)
        db.session.commit()
    except Exception as err:
        raise err


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


def read_all_orders():
    return PurchaseOrder.query.filter_by(status='UNFILLED')


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
        results = db.engine.execute(query)
    except Exception as err:
        raise err

    return results
