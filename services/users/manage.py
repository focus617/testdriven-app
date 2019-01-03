# services/users/manage.py


import unittest

from flask.cli import FlaskGroup
import coverage
import click
from flask_migrate import Migrate, MigrateCommand

from project import create_app, db
from project.api.models import User, Post


COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()

"""
Create a new FlaskGroup instance to extend the normal CLI with commands related 
to the Flask app, in order to run and manage the app from the command line
"""
app = create_app()
cli = FlaskGroup(create_app=create_app)

migrate = Migrate(app, db)
cli.add_command('db', MigrateCommand)


# shell context for flask cli, which is used to register the app and db
# to the shell.
# so we can work with the application context and the database without
# having to import them directly into the shell
@app.shell_context_processor
def ctx():
    return {'app': app, 'db': db, 'User': User, 'Post': Post}


@cli.command()
def recreate_db():
    """
    This registers a CLI command: recreate_db, so that we can run it from
    the command line, which we'll use to apply the model to the database.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()
    click.echo('Database Initialized!')


@cli.command()
def seed_db():
    """Seeds the database."""
    user_1 = User(username='Michael', email="michael@mherman.org")
    user_1.set_password('admin')
    db.session.add(user_1)

    user_2 = User(username='Xu Zhiyong', email="zhxu@163.com")
    user_2.set_password('admin')
    db.session.add(user_2)

    db.session.commit()
    click.echo('Database for User Initialized with some data!')


@cli.command()
def test():
    """
    This register a CLI command: test, to discover and run the tests.
    Note: Runs the tests without code coverage ...
    """
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1


if __name__ == '__main__':
    cli()
