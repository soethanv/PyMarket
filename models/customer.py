from setup import db


class Customer(db.Model):
    __tablename__ = 'Customer'
    customerID = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    phoneNum = db.Column(db.String(64))
    creditCardID = db.relationship('CreditCard', backref='customer', lazy=True)
    addressID = db.relationship('Address', backref='customer', lazy=True)

    def __init__(self, email, name):
        self.email = email
        self.name = name

    def __repr__(self):
        return '<Customer: {}, customer: {}>'.format(self.customerID, self.email)
