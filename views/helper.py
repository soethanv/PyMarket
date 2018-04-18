from views.user_auth import bp as user_auth_bp
from views.dashboard import bp as dashboard_bp
from views.sales import bp as sales_bp
from views.inventory import bp as inventory_bp

all_blueprints = (user_auth_bp, dashboard_bp, sales_bp, inventory_bp)
