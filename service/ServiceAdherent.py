from kendoDAO.AdherentsDAO import AdherentsDAO
from kendoDAO.GradesDAO import GradesDAO


class ServiceAdherent():
    def __init__(self, adherent):
        self.adherent = adherent
        self.adherentDAO = AdherentsDAO()
        self.gradeDAO = GradesDAO()

    def ajouterDiplome(self, libelleDiplome):
        self.gradeDAO.insertGrade(libelleDiplome, self.adherent.licence)


