from setup import db
from datetime import datetime


class IncomingTransaction(db.Model):
    __tablename__ = 'IncomingTransaction'
    batchID = db.Column(db.Integer, primary_key=True)
    SKU = db.Column(db.Integer, nullable=False)
    producer = db.Column(db.String(32), nullable=False)
    transactionDate = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


    def __init__(self, batchID, SKU, producer):
        self.batchID = batchID
        self.SKU = SKU
        self.producer = producer


    def __repr__(self):
        return '<IncomingTransaction {}>'.format(self.incTransactionID)
