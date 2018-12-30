# services/users/manage.py


import unittest

from flask.cli import FlaskGroup
import coverage

from project import create_app, db
from project.api.models import User


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


@cli.command()
def recreate_db():
    """
    This registers a CLI command: recreate_db, so that we can run it from
    the command line, which we'll use to apply the model to the database.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def seed_db():
    """Seeds the database."""
    db.session.add(User(username='michael', email="michael@mherman.org"))
    db.session.add(User(username='zhxu', email="zhxu@163.com"))
    db.session.commit()


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
