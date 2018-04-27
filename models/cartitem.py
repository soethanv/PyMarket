from setup import db


class CartItem(db.Model):
    __tablename__ = 'CartItem'
    cartItemID = db.Column(db.Integer, primary_key=True)
    SKU = db.Column(db.Integer, nullable=False)
    cartID = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, SKU, cartID, quantity):
        self.SKU = SKU
        self.cartID = cartID
        self.quantity = quantity

    def __repr__(self):
        return '<CartItem {}, cartID: {}>'.format(self.SKU, self.cartID)
