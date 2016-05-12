from kendoDAO.AdherentsDAO import AdherentsDAO
from kendoDAO.GradesDAO import GradesDAO
from models import Adherent, Grade

"""
Cette classe a pour utilité de gerer un adherent.
Il s'occupe de la communication avec les dao
"""
class ServiceAdherent():
    """
    constructeur
    """
    def __init__(self, adherent):
        self.adherent = adherent
        self.adherentDAO = AdherentsDAO()
        self.gradeDAO = GradesDAO()
        if self.adherent is None:
            raise AttributeError("Le service Adherent à besoin d'un objet Adherent")
        elif type(adherent) is not Adherent:
            raise AttributeError("Le service Adherent à besoin d'un objet Adherent")


    """
    s'occupe de l'ajout des grades pour un Adherent
    Args : libelleGrade - String
    """
    def ajouterGrade(self, libelleGrade):
        self.gradeDAO.insertGrade(libelleGrade, self.adherent.licence)

    def ajouterGradeWithAllInfo(self, libelle, date):
        grade = Grade(libelle, self.adherent.licence, date)
        self.gradeDAO.insertObject(grade)

    def supprimerGrade(self, id):
        grade = self.gradeDAO.findById(id)
        self.gradeDAO.delete(grade)

    def modifierProfesseur(self, nom, prenom, datenaissance):
        self.adherent.nom = nom
        self.adherent.prenom = prenom
        self.adherent.dateNaissance = datenaissance
        self.adherentDAO.update(self.adherent)


