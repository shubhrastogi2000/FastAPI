from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'      # when connecting with sqllite3 server
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args = {'check_same_thread':False})  # it allow only one thread to communicate with SQLite


# library neede - psycopg2-binary
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:mnb12345@localhost/TodoApplicationDatabase'   # when connect with postgresql
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

#library needed - pymysql
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:<password>@127.0.0.1:3386/TodoApplicationDatabase'   # when connect with MySQL
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind = engine)  # so that anything not done automatically and have full control of DB

Base = declarative_base()