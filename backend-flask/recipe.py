#!env/bin/python

import click
import unittest
from flask import Flask
from flask.cli import AppGroup

from app import app

user_cli = AppGroup('user')

@user_cli.command('test')
def test():
    pass

app.cli.add_command(user_cli)