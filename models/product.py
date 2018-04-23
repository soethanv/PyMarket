from setup import db


class Product(db.Model):
    __tablename__ = 'Product'
    SKU = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), index=True, unique=True, nullable=False)
    category = db.Column(db.String(16), nullable=False)
    price = db.Column(db.Numeric(4,2), nullable=False)
    reorder_point = db.Column(db.Integer, nullable=False)
    stock_quantity = db.Column(db.Integer, default=0, nullable=False)
    storage_location = db.Column(db.String(24), nullable=False)
    batches = db.relationship('ProductBatch', backref='product', lazy=True)

    def __init__(self, SKU, name, category, price, reorder_point, storage_location):
        self.SKU = SKU
        self.name = name
        self.category = category
        self.price = price
        self.reorder_point = reorder_point
        self.storage_location = storage_location


    def __repr__(self):
        return '<Product {}, {}>'.format(self.SKU, self.name)


    def update_stock_quantity(self):
        total = 0
        for batch in self.batches:
            total += batch.batch_quantity

        self.stock_quantity = int(total)
