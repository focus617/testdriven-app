# services/users/manage.py


from flask.cli import FlaskGroup

from project import app

"""
Create a new FlaskGroup instance to extend the normal CLI with commands related 
to the Flask app, in order to run and manage the app from the command line
"""
cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()
