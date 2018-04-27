from setup import db


class ShoppingCart(db.Model):
    __tablename__ = 'ShoppingCart'
    cartID = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.Integer, nullable=False)

    def __init__(self, customerId):
        self.customerID = customerId


    def __repr__(self):
        return '<ShoppingCart: {}, customer: {}>'.format(self.cartID, self.customerID)
