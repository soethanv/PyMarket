from setup import db


class CreditCard(db.Model):
    __tablename__ = 'CreditCard'
    creditCardID = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.Integer, db.ForeignKey('Customer.customerID'), nullable=False)
    ccCompany = db.Column(db.String(100), nullable=False)
    ccNum = db.Column(db.String(30), nullable=False)
    ccExpDt = db.Column(db.String(30), nullable=False)

    def __init__(self, customerID, ccCompany, ccNum, ccExpDt):
        self.customerID = customerID
        self.ccCompany = ccCompany
        self.ccNum = ccNum
        self.ccExpDt = ccExpDt

    def __repr__(self):
        return '<CreditCard: {}, customer: {}>'.format(self.creditCardID, self.customerID)
