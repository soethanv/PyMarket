from setup import db
from datetime import datetime

class ProductBatch(db.Model):
    __tablename__ = 'ProductBatch'
    batchID = db.Column(db.Integer, primary_key=True)
    SKU = db.Column(db.Integer, db.ForeignKey('Product.SKU'), nullable=False)
    producer = db.Column(db.String(24), nullable=False)
    batch_quantity = db.Column(db.Integer, nullable=False)
    batch_expiration = db.Column(db.DateTime, nullable=False)


    def __init__(self, SKU, producer, batch_quantity, batch_expiration):
        self.SKU = SKU
        self.batch_quantity = batch_quantity
        self.producer = producer

        # datetime.datetime(year, month, day)
        self.batch_expiration = batch_expiration


    def __repr__(self):
        return '<ProductBatch {}, {}>'.format(self.batchID, self.SKU)
