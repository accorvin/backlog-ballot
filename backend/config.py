import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    if 'DATABASE_URL' in os.environ:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    elif 'POSTGRESQL_USER' in os.environ and\
            'POSTGRESQL_PASSWORD' in os.environ and\
            'POSTGRESQL_DB' in os.environ and\
            'POSTGRESQL_HOST' in os.environ:
        user = os.environ['POSTGRESQL_USER']
        pw = os.environ['POSTGRESQL_PASSWORD']
        db = os.environ['POSTGRESQL_DB']
        host = os.environ['POSTGRESQL_HOST']
        SQLALCHEMY_DATABASE_URI = ('postgresql://{user}:{pw}@{host}:'
                                   '5432/{db}').format(user=user,
                                                       pw=pw,
                                                       host=host,
                                                       db=db)

    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                                                              'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
