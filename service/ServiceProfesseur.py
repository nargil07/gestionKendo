from kendoDAO.DiplomesDAO import DiplomesDAO
from kendoDAO.ProfesseursDAO import ProfesseursDAO


class ServiceProfesseur():
    def __init__(self, professeur):
        self.professeur = professeur
        self.professeurDAO = ProfesseursDAO()
        self.diplomesDAO = DiplomesDAO()

    def ajouterDiplome(self, libelleGrade):
        self.diplomesDAO.insert(libelleGrade, self.professeur.licence)