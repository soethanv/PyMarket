# PyMarket


## Contributors

  - Carter Hunter
  - Dalton Sumrall
  - Gustavo Chavez
  - Julia Vasquez
  - Soe Than


## Storage Portal Features

  - Quick view of items that are about to expire and are reaching their reorder point
  - Easily view unfilled orders and the products needed to complete them
  - Sort, Edit, and Search Product information in the inventory
  - Automatic quantity update when incoming inventory batches are added
  - Automatic tracking of incoming/outgoing transaction history


##  Setup Dependencies

Our portal was tested on linux using python3 and Flask web framework. We wrote a setup bash script to easily download all dependencies and setup up the python virtual environment. It requires the user have bash, python3, and pip. When ran the script will create a python virtual environment, download all dependencies in requirements.txt, set up flask env variables, and then enter the user into the virtual environment. To execute:
```
> . project_init.sh
```
Take note of the "." when running the script. It enables the script to enter you into the virtual environment and set the correct FLASK_APP env variable in your current shell.


## Alternative Setup

If the setup script fails to work, use the following commands to setup.
```
> virtualenv venv
> source ./venv/bin/activate
> pip install -r requirements.txt
> export FLASK_APP=application.py
```


## Running the Flask App

To run:
```
> flask run
 * Serving Flask app "application"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Open a browser and visit the url it provides. (or ctrl-click the url)


## Optional: Build the Database

If for some reason the database gets deleted or has errors, it can be rebuilt by doing the following:
```
> flask db init
> flask db migrate -m "database init"
> flask db upgrade
> python3 populate_db.py
```


## Optional: Repopulate the Database

If the database has had a lot of deletions you can easily add the sample data back to it by running:
```
> python3 populate_db.py
```
It will delete all the data in the tables and repopulate them with the original samples.


## Sign in

We provided a guest account to sign in:
```
Username: guest
Password: 1L23!hpx$W
```
If you try to visit a page before logging in it will redirect you to the sign in page. Once you successfully sign in it will redirect you back to the page you tried to visit.


## Dashboard

Once you're logged in you will see the Dashboard page. Here you will see a quick view of things that need attention, items that are expiring soon and products that need reordering.

We provided a navigation bar at the top to easily traverse to the other pages.


## Inventory Page

On this page you are able to see all products the store offers and their information. You can click on the **+** button next to a product to view all of the batches of that product type. If a batch is expiring soon (within 7 days) it is highlighted yellow. If you delete or add a batch to a product the product's inventory quantity will be updated automatically. The data tables we are using also enable the user to search for information, as well as sort by column.


## Orders page

On this page you are able to view all of the orders that are awaiting fulfillment. You can click on the **+** button next to an order to view all of the products that the order consists of. The items can be checked to indicate that an employee has already retrieved the item from storage and put in the "*shipping box*" for the customer. When an item is checked off it is automatically logged in the database outgoing transactions table, thus keep track of all outgoing shipments.

Once all items have been check off the employee can change the status of the order to "*FILLED*", so some other part of the system can assign it to a delivery driver. Once the order is filled it won't show up on the orders page so the storage manager can focus on only unfilled orders.


## Incoming/Outgoing Transaction page

On these pages the storage manager is able to see all the incoming/outgoing transaction history. The incoming transactions are logged when a batch is added to the inventory. The outgoing transactions are logged when an item is marked as filled in the orders page.
