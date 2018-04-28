from setup import db


class IncomingTransaction(db.Model):
    __tablename__ = 'IncomingTransaction'
    incTransactionID = db.Column(db.Integer, primary_key=True)
    SKU = db.Column(db.Integer, nullable=False)
    batchID = db.Column(db.Integer, unique=True, nullable=False)
    producer = db.Column(db.String(32), nullable=False)
    transactionDate = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)


    def __init__(self, SKU, batchID, producer, transactionDate):
        self.SKU = SKU
        self.batchID = batchID
        self.producer = producer
        self.transactionDate = transactionDate


    def __repr__(self):
        return '<IncomingTransaction {}>'.format(self.incTransactionID)
