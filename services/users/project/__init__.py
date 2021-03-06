#!/usr/bin/env python
# -*- coding:utf-8 -*
# @Author   : Zhxu
# @Time     : 18-12-28 下午9:50

# services/users/project/__init__.py

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
from flask_login import LoginManager


# instantiate the extensions, including db, debugToolbar, loginManager
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
login = LoginManager()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up Flask-SQLAlchemy extensions
    db.init_app(app)

    # set up DebugToolbar extensions
    toolbar.init_app(app)

    # set up the Flask-Login extension
    login.init_app(app)
    login.login_view = 'blog.login'

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    from project.api.microblog import blog_blueprint
    app.register_blueprint(blog_blueprint)

    # # shell context for flask cli, which is used to register the app and db
    # # to the shell.
    # # so we can work with the application context and the database without
    # # having to import them directly into the shell
    # @app.shell_context_processor
    # def ctx():
    #     return {'app': app, 'db': db, 'User': User, 'Post': Post}

    return app
