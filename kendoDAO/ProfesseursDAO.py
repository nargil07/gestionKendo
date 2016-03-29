from kendoDAO.AbstractDAO import DAO
from models import Professeur

class ProfesseursDAO(DAO):

    def findAll(self):
        professeurs = []
        for professeur in self.session.query(Professeur):
            professeurs.append(professeur)
        return professeurs

    def insert(self, licence, nom, prenom, dateNaissance):
        professeur = Professeur(licence, nom, prenom, dateNaissance)
        self.session.add(professeur)
        self.session.commit()