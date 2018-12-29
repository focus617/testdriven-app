#!/usr/bin/env python
# -*- coding:utf-8 -*
# @Author   : Zhxu
# @Time     : 18-12-29 下午2:49

# services/users/project/tests/base.py


from flask_testing import TestCase

from project import app, db


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
