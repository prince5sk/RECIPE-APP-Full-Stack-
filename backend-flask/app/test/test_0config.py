# app/main/test test_config.py

import os
import unittest

from flask import current_app
from flask_testing import TestCase

from recipe import app
from app.config import BASE_DIR


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'yOu-WiLl-nEveR-GUesS')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' +
            os.path.join(BASE_DIR, 'app.db')
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'yOu-WiLl-nEveR-GUesS')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' +
            os.path.join(BASE_DIR, 'app_test.db')
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertFalse(app.config['DEBUG'])


if __name__ == '__main__':
    unittest.main()
