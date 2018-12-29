# services/users/manage.py


import unittest

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import User

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


if __name__ == '__main__':
    cli()
