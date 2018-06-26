from api import create_app, db
from api.models import Issue

app = create_app()


# Set up the database objects to be available when running the
# Flask shell. This makes it much easier to interact with the database.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Issue': Issue}
