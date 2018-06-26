import logging
import sys

from config import Config
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def insert_headers(response):
    """
    Insert configured HTTP headers into the Flask response.
    :param flask.Response response: the response to insert headers into
    :return: modified Flask response
    :rtype: flask.Response
    """
    cors_url = '*'
    if cors_url:
        response.headers['Access-Control-Allow-Origin'] = cors_url
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Method'] = '*'
    return response


def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from api.issues import bp as issues_bp
    app.register_blueprint(issues_bp, url_prefix='/api/issues')

    from api.health import bp as health_bp
    app.register_blueprint(health_bp, url_prefix='/api/health')

    if not app.debug and not app.testing:
        log = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(('%(asctime)s - %(name)s - '
                                       '%(levelname)s - %(message)s'))
        log.setFormatter(formatter)
        log.setLevel(logging.INFO)
        app.logger.addHandler(log)
        app.logger.setLevel(logging.INFO)

        app.after_request(insert_headers)

    return app
