from application import application
from setup import db
from sqlalchemy import text
from datetime import date
from models.user import User
from models.customer import Customer
from models.address import Address
from models.creditcard import CreditCard
from models.shoppingcart import ShoppingCart
from models.cartitem import CartItem
from models.purchaseorder import PurchaseOrder
from models.crud_operations import read_all_products, create_product_batch, create_product

with application.app_context():

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

    for user in user_list:
        db.session.add(user)

    db.session.commit()



    create_product(1234, 'Granny Apple', 'Fruit', 0.10, 100, '01-02-01')
    create_product(7384, 'Cutie Orange', 'Fruit', 0.15, 150, '01-01-01')
    create_product(90821, 'Awesome Sauce Hot Sauce', 'Condiment', 4.00, 50, '03-03-01')
    create_product(2321, 'Best Protein Bagels', 'Bread', 5.00, 75, '02-06-03')
    create_product(4326, 'Kobe Beef Burgers', 'Meat', 15.00, 50, '04-01-01')


    create_product_batch(1234, 'ProducerA', 50, 2018, 6, 15)
    create_product_batch(7384, 'ProducerB', 75, 2018, 6, 8)
    create_product_batch(90821, 'ProducerC', 5, 2019, 5, 10)
    create_product_batch(2321, 'ProducerD', 15, 2018, 5, 4)
    create_product_batch(4326, 'ProducerE', 30, 2018, 5, 4)

    create_product_batch(1234, 'ProducerF', 20, 2018, 7, 15)
    create_product_batch(7384, 'ProducerG', 40, 2018, 7, 8)
    create_product_batch(90821, 'ProducerH', 5, 2019, 5, 10)
    create_product_batch(2321, 'ProducerI', 15, 2018, 5, 15)
    create_product_batch(4326, 'ProducerJ', 10, 2018, 5, 11)

    create_product_batch(1234, 'ProducerK', 20, 2018, 8, 15)
    create_product_batch(7384, 'ProducerL', 40, 2018, 8, 8)
    create_product_batch(90821, 'ProducerM', 10, 2019, 5, 10)
    create_product_batch(2321, 'ProducerN', 15, 2018, 5, 25)
    create_product_batch(4326, 'ProducerO', 10, 2018, 5, 15)

    create_product_batch(1234, 'ProducerP', 20, 2018, 9, 15)
    create_product_batch(7384, 'ProducerQ', 40, 2018, 9, 8)
    create_product_batch(90821, 'ProducerR', 5, 2019, 5, 10)
    create_product_batch(2321, 'ProducerS', 15, 2018, 6, 2)
    create_product_batch(4326, 'ProducerT', 10, 2018, 5, 20)

    create_product_batch(1234, 'ProducerU', 20, 2018, 10, 15)
    create_product_batch(7384, 'ProducerV', 40, 2018, 5, 6)
    create_product_batch(90821, 'ProducerW', 5, 2019, 5, 10)
    create_product_batch(2321, 'ProducerX', 15, 2018, 6, 10)
    create_product_batch(4326, 'ProducerY', 10, 2018, 5, 23)



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
