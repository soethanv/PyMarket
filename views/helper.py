from views.user_auth import bp as user_auth_bp
from views.dashboard import bp as dashboard_bp
from views.orders import bp as orders_bp
from views.inventory import bp as inventory_bp
from views.transaction import bp as transaction_bp

all_blueprints = (user_auth_bp, dashboard_bp, orders_bp, inventory_bp, transaction_bp)
