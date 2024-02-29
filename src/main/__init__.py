"""Flask Application"""

from flask import Flask
from flask_graphql import GraphQLView 
from flask_cors import CORS



from .config import config_by_name   
from .database.db_session import db_session
from .schema.schema import schema
from .models.User import User
from .utils.extensions import bcrypt ,jwt 
 
def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])    
    bcrypt.init_app(app)
    jwt.init_app(app) 
    
    app.config['CORS_RESOURCE'] = r"/graphql/*"
    app.config['CORS_ORIGINS'] = app.config['CORS_ORIGINS']
    # app.config['CORS_ALLOW_HEADERS '] =  'Content-Type'
    # app.config['CORS_METHODS'] = ["GET", "HEAD", "POST", "OPTIONS", "PUT", "PATCH", "DELETE"]
    cors = CORS(app)

    # Register a callback function that takes whatever object is passed in as the
    # identity when creating JWTs and converts it to a JSON serializable format.
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user


    # Register a callback function that loades a user from your database whenever
    # a protected route is accessed. This should return any python object on a
    # successful lookup, or None if the lookup failed for any reason (for example
    # if the user has been deleted from the database).
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(username=identity).one_or_none()


    @app.after_request
    def after_request(response): 
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    @app.teardown_request
    def session_clear(exception=None):
        db_session.remove()
        if exception and db_session.is_active:
            db_session.rollback()
            
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=False, 
            get_context=lambda: {'session': db_session()}
        )
    ) 
 
        
    return app 