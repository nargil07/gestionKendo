from models import Professeur
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
class ProfesseursDAO():
    def __init__(self):
        self.session = None
        try:
            engine = create_engine('sqlite:///bd.db', echo=True)
            Session = sessionmaker(bind=engine)
            self.session = Session()
        except Exception as err:
            raise Exception(err.message)

    def findAll(self):
        professeurs = []
        for professeur in self.session.query(Professeur):
            professeurs.append(professeur)
        return professeurs

    def insert(self, licence, nom, prenom, dateNaissance):
        professeur = Professeur(licence, nom, prenom, dateNaissance)
        self.session.add(professeur)
        self.session.commit()