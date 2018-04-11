from views.login import bp as login_bp
from views.dashboard import bp as dashboard_bp
from views.logout import bp as logout_bp

all_blueprints = (login_bp, dashboard_bp, logout_bp)
