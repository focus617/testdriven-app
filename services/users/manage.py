# services/users/manage.py


from flask.cli import FlaskGroup

from project import app

"""
Create a new FlaskGroup instance to extend the normal CLI with commands related 
to the Flask app, in order to run and manage the app from the command line
"""
cli = FlaskGroup(app)


"""
This registers a new command, recreate_db, to the CLI so that we can run it from 
the command line, which we'll use to apply the model to the database.
"""
@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
