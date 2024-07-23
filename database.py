from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'mysql+pymysql://rishik12:rishik123@localhost:3306/blogapplication'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False,autoflush=False, bind=engine)

Base = declarative_base()