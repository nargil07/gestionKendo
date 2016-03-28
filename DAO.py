import os.path
from datetime import date
from models import Adherent
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
class DAO():
    def __init__(self, dbName = "bd.db"):
        self.dbName = dbName
        self.session = None
        print dbName
        try:
            engine = create_engine('sqlite:///bd.db', echo=True)

            Session = sessionmaker(bind=engine)
            self.session = Session()
            test = self.session.query(Adherent)
            print(test)
        except Exception as err:
            raise Exception(err.message)

if __name__ == "__main__":

    dao = DAO()
    print(dao)


