from models.user import User
from models.product import Product
from models.customer import Customer
from models.address import Address
from models.creditcard import CreditCard
from models.shoppingcart import ShoppingCart
from models.cartitem import CartItem
from models.product import Product
from models.productbatch import ProductBatch
from models.purchaseorder import PurchaseOrder
from models.incomingtransaction import IncomingTransaction
from models.outgoingtransaction import OutgoingTransaction

model_classes = {
    'User': User,
    'Product': Product,
    'Customer': Customer,
    'Address': Address,
    'CreditCard': CreditCard,
    'ShoppingCart': ShoppingCart,
    'CartItem': CartItem,
    'Product': Product,
    'ProductBatch': ProductBatch,
    'PurchaseOrder': PurchaseOrder,
    'IncomingTransaction': IncomingTransaction,
    'OutgoingTransaction': OutgoingTransaction
}
