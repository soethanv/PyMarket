from application import main_application
from setup import db
from sqlalchemy import text
from models.user import User
from models.customer import Customer
from models.address import Address
from models.creditcard import CreditCard
from models.product import Product
from models.shoppingcart import ShoppingCart
from models.cartitem import CartItem
from models.purchaseorder import PurchaseOrder


with main_application.app_context():

    # delete all rows in database before executing
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table %s' % table)
        db.session.execute(table.delete())
    db.session.commit()


    # Add users into database
    user_list = [
        User('dalton', 'aog729'),
        User('julia', 'dpo131'),
        User('soe', 'cvt133'),
        User('gus', 'uwe880'),
        User('carter', 'qja551'),
        User('guest', '1L23!hpx$W')
    ]


    product_list = [
        Product(1234, 'Granny Apple', 'Fruit', 0.10, 100, 200, '01-02-01'),
        Product(7384, 'Cutie Orange', 'Fruit', 0.15, 150, 250, '01-01-01'),
        Product(90821, 'Awesome Sauce Hot Sauce', 'Condiment', 4.00, 50, 65, '03-03-01'),
        Product(2321, 'Best Protein Bagels', 'Bread', 5.00, 75, 100, '02-06-03'),
        Product(4326, 'Kobe Beef Burgers', 'Meat', 15.00, 50, 75, '04-01-01')
    ]

    for user in user_list:
        db.session.add(user)

    for product in product_list:
        db.session.add(product)

    db.session.commit()


    ############################### Customer 1 ###############################

    customer = Customer('dwightschrute@gmail.com', 'Dwight Schrute')
    db.session.add(customer)
    db.session.commit()

    address = Address(customer.customerID, 'Schrute Farms', 'Scranton', 'PA', '18503', 'USA')
    card = CreditCard(customer.customerID, 'Farm House', '123456789', '2018-09-09')
    db.session.add(address)
    db.session.add(card)
    db.session.commit()

    cart = ShoppingCart(customer.customerID)
    db.session.add(cart)
    db.session.commit()

    cart_item_list = [
        CartItem(90821, cart.cartID, 2),
        CartItem(1234, cart.cartID, 25),
        CartItem(2321, cart.cartID, 1)
    ]

    for item in cart_item_list:
        db.session.add(item)

    db.session.commit()

    query = ('SELECT p.price, ci.quantity '
             'FROM CartItem ci, Product p '
             'WHERE ci.cartID = ' + str(cart.cartID) + ' and ci.SKU = p.SKU'
            )
    query = text(query)
    results = db.engine.execute(query)

    total_price = 0
    for item in results:
        total_price = total_price + (item[0] * item[1])

    purchase_order = PurchaseOrder(cart.cartID, customer.customerID, total_price)
    db.session.add(purchase_order)
    db.session.commit()

    ##########################################################################


    ############################### Customer 2 ###############################

    customer = Customer('michealscott@gmail.com', 'Micheal Scott')
    db.session.add(customer)
    db.session.commit()

    address = Address(customer.customerID, 'Expensive Condos', 'Scranton', 'PA', '18503', 'USA')
    card = CreditCard(customer.customerID, 'Scranton Bank', '987654321', '2020-11-02')
    db.session.add(address)
    db.session.add(card)
    db.session.commit()

    cart = ShoppingCart(customer.customerID)
    db.session.add(cart)
    db.session.commit()

    cart_item_list = [
        CartItem(4346, cart.cartID, 10),
        CartItem(7384, cart.cartID, 40),
        CartItem(90821, cart.cartID, 3)
    ]

    for item in cart_item_list:
        db.session.add(item)

    db.session.commit()

    query = ('SELECT p.price, ci.quantity '
             'FROM CartItem ci, Product p '
             'WHERE ci.cartID = ' + str(cart.cartID) + ' and ci.SKU = p.SKU'
            )
    query = text(query)
    results = db.engine.execute(query)

    total_price = 0
    for item in results:
        total_price = total_price + (item[0] * item[1])

    purchase_order = PurchaseOrder(cart.cartID, customer.customerID, total_price)
    db.session.add(purchase_order)
    db.session.commit()

    ##########################################################################
