from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///musicLibrary.db', echo=True)
Base = declarative_base(engine)
Session = sessionmaker()
Session.configure(bind=engine)