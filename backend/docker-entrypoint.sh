#!/bin/sh

while true; do
    echo "Attempting to upgrade the database"
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

if [ -n $FLASK_DEBUG ]; then
    flask run --host=0.0.0.0 --port=5000
else
    # Run gunicorn, a production-ready Flask server.
    # Listen on all interfaces at port 5000
    # Direct the access and error logs to standard out
    # Tell gunicorn that the Flask app can be found in the app.py module as
    #   the app object.
    exec gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - app:app
fi
