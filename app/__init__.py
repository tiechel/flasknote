from flask import Flask
from config import Config
from flask_migrate import Migrate
from app.models import db

migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.main.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
