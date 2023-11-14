import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

from dotenv import (load_dotenv, find_dotenv)
load_dotenv(find_dotenv(os.path.join(BASE_DIR , '.env')))

SPOONACULAR_API_KEY = os.getenv('SPOONACULAR_API_KEY')

DATABASE_URI = 'sqlite:///' + \
    os.path.join(BASE_DIR, 'app.db')

TEMPLATES_FOLDER = \
    os.path.join(BASE_DIR, os.environ.get('TEMPLATES_FOLDER', 'templates'))