#!env/bin/python

import click
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask.cli import AppGroup

from app import app
from app.main import db

user_cli = AppGroup('user')

migrate = Migrate(app, db)

@app.cli.command('test')
def test():
    """ Runs the unit tests """
    tests = unittest.TestLoader().discover('app/test', pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

app.cli.add_command(user_cli)