from datetime import datetime
from setup import db


class PurchaseOrder(db.Model):
    __tablename__ = 'PurchaseOrder'
    poID = db.Column(db.Integer, primary_key=True)
    cartID = db.Column(db.Integer, nullable=False)
    customerID = db.Column(db.Integer, nullable=False)
    totalOrderPrice = db.Column(db.Numeric(6,2), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    createdDt = db.Column(db.DateTime, default=datetime.utcnow)
    lastUpdatedDt = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, cartID, customerID, totalOrderPrice):
        self.cartID = cartID
        self.customerID = customerID
        self.totalOrderPrice = totalOrderPrice
        self.status = 'UNFILLED'

    def __repr__(self):
        return '<PurchaseOrder: {}, customer: {}>'.format(self.poID, self.customerID)
