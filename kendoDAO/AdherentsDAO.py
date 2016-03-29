# coding=utf-8
from kendoDAO.AbstractDAO import DAO
from models import Adherent

class AdherentsDAO(DAO):

    def findAll(self):
        adherents = []
        for adherent in self.session.query(Adherent):
            adherents.append(adherent)
        return adherents

    def insert(self, nom, prenom, dateNaissance):
        adherent = Adherent()
        pass
    """
    Permet de recuperer un etudiant
    Si il ne trouve pas d'étudiant renvoie None
    Returns : Etudiant | None
    """
    def findById(self, id):
        return self.session.query(Adherent).filter(Adherent.licence == id).one_or_none()