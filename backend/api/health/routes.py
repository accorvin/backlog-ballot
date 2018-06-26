from api.health import bp
from flask import jsonify


# Define a route and the endpoint that it's availalbe at
# Multiple url endpoints are allowed.
@bp.route('/status')
def healthcheck():
    response_object = {
        'code': 'success',
        'description': 'I am healthy'
    }
    return jsonify(response_object), 200
