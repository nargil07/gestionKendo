from kendoDAO.DiplomesDAO import DiplomesDAO
from kendoDAO.GradesDAO import GradesDAO
from kendoDAO.ProfesseursDAO import ProfesseursDAO
from models import Professeur, Diplome, Grade


class ServiceProfesseur():
    """
    Cette classe a pour utilité la gestion d'un professeur
    Il s'occupe de la communication avec les dao
    """

    def __init__(self, professeur):
        """
        constructeur
        """
        self.professeur = professeur
        self.professeurDAO = ProfesseursDAO()
        self.diplomesDAO = DiplomesDAO()
        self.gradesDAO = GradesDAO()
        if (self.professeur is None):
            raise AttributeError("Le service professeur à besoin d'un objet Professeur")
        elif type(professeur) is not Professeur:
            raise AttributeError("Le service professeur à besoin d'un objet Professeur")

    def ajouterDiplome(self, libelleDiplome):
        """
        Permet d'ajouter un diplome a  un professeur
        """
        self.diplomesDAO.insert(libelleDiplome, self.professeur.licence)

    def ajouterDiplomeWithAllInfo(self, libelle, date):
        diplome = Diplome(libelle, self.professeur.licence, date)
        self.diplomesDAO.insertObject(diplome)

    def supprimerDiplome(self, id):
        diplome = self.diplomesDAO.findById(id)
        self.diplomesDAO.delete(diplome)