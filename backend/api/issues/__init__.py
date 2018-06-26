from flask import Blueprint

bp = Blueprint('issues', __name__)

from api.issues import routes  # noqa: E402,F401
