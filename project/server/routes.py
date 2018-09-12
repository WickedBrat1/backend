from flask import Blueprint

from project.server.auth import auth_views

auth_blueprint = Blueprint('auth', __name__)

auth_blueprint.add_url_rule(
    '/api/auth/register',
    view_func=auth_views.registration_view,
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/api/auth/login',
    view_func=auth_views.login_view,
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/api/auth/status',
    view_func=auth_views.user_view,
    methods=['GET']
)
auth_blueprint.add_url_rule(
    '/api/auth/logout',
    view_func=auth_views.logout_view,
    methods=['POST']
)
