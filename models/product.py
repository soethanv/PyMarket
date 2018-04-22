from setup import db


class Product(db.Model):
    __tablename__ = 'Product'
    SKU = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), index=True, unique=True, nullable=False)
    category = db.Column(db.String(16), nullable=False)
    price = db.Column(db.Numeric(4,2), nullable=False)
    reorder_point = db.Column(db.Integer, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    storage_location = db.Column(db.String(24), nullable=False)


    def __init__(self, SKU, name, category, price, reorder_point, stock_quantity, storage_location):
        self.SKU = SKU
        self.name = name
        self.category = category
        self.price = price
        self.reorder_point = reorder_point
        self.stock_quantity = stock_quantity
        self.storage_location = storage_location


    def __repr__(self):
        return '<Product {}, {}>'.format(self.SKU, self.name)
