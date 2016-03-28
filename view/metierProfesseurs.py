from kendoDAO.ProfesseursDAO import ProfesseursDAO


class MetierProfesseurs():
    def __init__(self):
        self.professeursDAO = ProfesseursDAO()
    def afficherProfesseurs(self):
        professeurs = self.professeursDAO.findAll()
        for professeur in professeurs:
            print("{} : {} {}".format(professeur.licence, professeur.prenom, professeur.nom))