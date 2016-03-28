from models import Adherent
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
class AdherentsDAO():
    def __init__(self):
        self.session = None
        try:
            engine = create_engine('sqlite:///bd.db', echo=True)
            Session = sessionmaker(bind=engine)
            self.session = Session()
        except Exception as err:
            raise Exception(err.message)
    def findAll(self):
        adherents = []
        for adherent in self.session.query(Adherent):
            adherents.append(adherent)
        return adherents