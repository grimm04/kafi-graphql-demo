# /books/database/db_session.py
from flask import current_app 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.engine.url import URL

# config = dict(
#     drivername=current_app.config['DRIVERNAME'],
#     username=current_app.config['USERNAME'],
#     password=current_app.config['PASSWORD'],
#     host=current_app.config['HOST'],
#     port=current_app.config['PORT'],
#     database=current_app.config['DATABASE'],
#     query=current_app.config['QUERY']
# )

# url = URL(**config) 
# print(url)
# engine = create_engine(url, convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

engine = create_engine('mysql+pymysql://root:@localhost/ws_kafiarchitect', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))