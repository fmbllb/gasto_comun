import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import DepartmentModel

db = SQLAlchemy()

# Configuración de logging
logging.basicConfig(level=logging.INFO)  # Cambié el nivel de logging a INFO para mensajes generales
logger = logging.getLogger(__name__)

class SingletonDB:
    _instance = None

    def __new__(cls, app=None):
        if cls._instance is None:
            try:
                cls._instance = super(SingletonDB, cls).__new__(cls)
                cls._instance.init_app(app)
            except Exception as e:
                logger.error("Error initializing SingletonDB: %s", e)
                raise
        return cls._instance

    def init_app(self, app):
        if app is not None:
            try:
                db.init_app(app)
                logger.info("Database initialized successfully.")
            except Exception as e:
                logger.error("Failed to initialize the database with the app context: %s", e)
                raise

def create_app():
    app = Flask(__name__)

    try:
        app.config.from_object('config.Config')  # Configuración de la base de datos desde config.py
        logger.info("App configuration loaded successfully.")
    except ImportError as e:
        logger.error("Configuration file not found: %s", e)
        raise RuntimeError("Configuration file is missing or misconfigured.") from e
    except Exception as e:
        logger.error("Error loading configuration: %s", e)
        raise RuntimeError("Error loading the configuration.") from e

    # Inicializar la instancia SingletonDB
    try:
        SingletonDB(app)
    except Exception as e:
        logger.error("Error creating the database singleton instance: %s", e)
        raise RuntimeError("Database initialization failed.") from e

    with app.app_context():
        try:
            from models import TaskModel  # Importar los modelos después de la inicialización de la base de datos
            db.create_all()  # Crea todas las tablas definidas en los modelos
            logger.info("Database tables created successfully.")
        except Exception as e:
            logger.error("Error creating database tables: %s", e)
            raise RuntimeError("Failed to create database tables.") from e

    logger.info("Application and database initialization completed successfully.")
    return app
