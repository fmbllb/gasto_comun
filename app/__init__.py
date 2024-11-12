from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instancia global de SQLAlchemy
db = SQLAlchemy()

# Instancia de Migrate
migrate = Migrate()

class SingletonDB:
    _instance = None

    def __new__(cls, app=None):
        if cls._instance is None:
            cls._instance = super(SingletonDB, cls).__new__(cls)
            cls._instance.init_app(app)
        return cls._instance

    def init_app(self, app):
        if app is not None:
            db.init_app(app)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Inicializamos el SingletonDB
    SingletonDB(app)  # Singleton instance of DB

    # Inicializamos Migrate
    migrate.init_app(app, db)

    with app.app_context():
        # Importamos los modelos después de la inicialización de la app
        from models import DepartmentModel, BillModel, PaymentHistoryModel

    return app
