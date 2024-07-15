from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from exceptions import ValidationError, NotFoundError, UnauthorizedError

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from .routes import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    # Register error handlers
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        response = jsonify({"error": str(error)})
        response.status_code = 400
        return response

    @app.errorhandler(NotFoundError)
    def handle_not_found_error(error):
        response = jsonify({"error": str(error)})
        response.status_code = 404
        return response

    @app.errorhandler(UnauthorizedError)
    def handle_unauthorized_error(error):
        response = jsonify({"error": str(error)})
        response.status_code = 401
        return response

    @app.errorhandler(500)
    def handle_internal_server_error(error):
        response = jsonify({"error": "An unexpected error occurred"})
        response.status_code = 500
        return response
