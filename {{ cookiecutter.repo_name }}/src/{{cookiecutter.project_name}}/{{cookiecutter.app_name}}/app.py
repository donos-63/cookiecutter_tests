from flask import Flask
from {{cookiecutter.app_name}} import api
from {{cookiecutter.app_name}} import auth
from {{cookiecutter.app_name}}.extensions import apispec
from {{cookiecutter.app_name}}.extensions import db
from {{cookiecutter.app_name}}.extensions import jwt
from {{cookiecutter.app_name}}.extensions import migrate

def create_app(testing=False):
    """Application factory, used to create application"""
    app = Flask("{{cookiecutter.app_name}}")
    app.config.from_object("{{cookiecutter.app_name}}.config")

    if testing is True:
        app.config["TESTING"] = True

    configure_extensions(app)
    configure_apispec(app)
    register_blueprints(app)

    return app


def configure_extensions(app):
    """configure flask extensions"""
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)


def configure_apispec(app):
    """Configure APISpec for swagger support"""
    apispec.init_app(app, security=[{"jwt": []}])
    apispec.spec.components.security_scheme(
        "jwt", {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    )
    apispec.spec.components.schema(
        "PaginatedResult",
        {
            "properties": {
                "total": {"type": "integer"},
                "pages": {"type": "integer"},
                "next": {"type": "string"},
                "prev": {"type": "string"},
            }
        },
    )


def register_blueprints(app):
    """register all blueprints for application"""
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)
