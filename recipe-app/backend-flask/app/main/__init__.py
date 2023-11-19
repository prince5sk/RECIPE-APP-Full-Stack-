# app/main/__init__

from flask import Flask
import app.settings as settings

import rq
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from app.config import config_by_name

db = SQLAlchemy()
migrate = Migrate(db)
bcrypt = Bcrypt()


def create_app(conifg_name) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[conifg_name])

    db.init_app(app)
    bcrypt.init_app(app)
    CORS(app)

    return app