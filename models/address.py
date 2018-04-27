from setup import db


class Address(db.Model):
    __tablename__ = 'Address'
    addressID = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.Integer, db.ForeignKey('Customer.customerID'), nullable=False)
    line1 = db.Column(db.String(100), nullable=False)
    line2 = db.Column(db.String(100))
    city = db.Column(db.String(32), nullable=False)
    state = db.Column(db.String(10), nullable=False)
    zipCode = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(20), nullable=False)


    def __init__(self, customerID, line1, city, state, zipCode, country):
        self.customerID = customerID
        self.line1 = line1
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.country = country

    def __repr__(self):
        return '<Address: {}, customer: {}>'.format(self.addressID, self.customerID)
