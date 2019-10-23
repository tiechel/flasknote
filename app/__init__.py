from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from config import Config
from flask_migrate import Migrate
from app.models import db, Entry

migrate = Migrate()
admin = Admin(name='flasknote', template_mode='bootstrap3')
admin.add_view(ModelView(Entry, db.session))


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)

    from app.main.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
