import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_URI = 'sqlite:///' + \
    os.path.join(BASE_DIR, 'app.db')

TEMPLATES_FOLDER = \
    os.path.join(BASE_DIR, os.environ.get('TEMPLATES_FOLDER', 'templates'))