from setup import db
from datetime import datetime


class OutgoingTransaction(db.Model):
    __tablename__ = 'OutgoingTransaction'
    outTransactionID = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.Integer, primary_key=True)
    SKU = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    from_batches = db.Column(db.String(128), nullable=False)
    transactionDate = db.Column(db.DateTime, nullable=False)


    def __init__(self, customerID, SKU, quantity, from_batches, transactionDate):
        self.customerID = customerID
        self.SKU = SKU
        self.quantity = quantity
        self.from_batches = from_batches
        self.transactionDate = transactionDate


    def __repr__(self):
        return '<OutgoingTransaction {}>'.format(self.outTransactionID)
