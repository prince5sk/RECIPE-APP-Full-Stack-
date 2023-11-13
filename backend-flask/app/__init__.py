# app/__init__

import eventlet
eventlet.monkey_patch()

import os
from dotenv import (load_dotenv, find_dotenv)
from app.settings import BASE_DIR

from app.main import create_app

load_dotenv(find_dotenv(os.path.join(BASE_DIR , '.env')))

from flask_restx import Api
from flask import Blueprint

# block:blueprints
# end-block:blueprints

# block:controllers
# end-block:controller

# block:models
from app.main.model import (
    user
)
# end-block:models

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint,
          title='Flask Recipe API',
          version='0.1',
          description='a recipe finder app')

# add namespaces here

app = create_app(os.getenv('ENV', 'dev'))
app.register_blueprint(blueprint)