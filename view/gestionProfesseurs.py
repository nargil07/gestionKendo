from datetime import datetime
from kendoDAO.ProfesseursDAO import ProfesseursDAO
from service.ServiceProfesseur import ServiceProfesseur


class GestionProfesseurs():
    def __init__(self):
        self.professeursDAO = ProfesseursDAO()

    def afficherProfesseurs(self):
        professeurs = self.professeursDAO.findAll()
        print("")
        for professeur in professeurs:
            print("{} : {} {}".format(professeur.licence, professeur.prenom, professeur.nom))
        print("")

    def afficherAjoutProfesseur(self):
        print("")
        nom = input("Nom : ")
        prenom = input("Prenom : ")
        dateNaissance = datetime.strptime(input("Date de naissance (JJ/MM/AAA) : "), "%d/%m/%Y")
        print("")
        self.professeursDAO.insert(nom, prenom, dateNaissance)

    def afficherAjoutDiplome(self):
        professeurs = self.professeursDAO.findAll()
        print("")
        print("A qui donner un diplome")
        for professeur in professeurs:
            print("{} : {} {} ".format(professeur.licence, professeur.prenom, professeur.nom))

        choixLicence = int(input("Tapez son numero de licence : "))
        professeur = self.professeursDAO.findById(choixLicence)
        print("")
        if (professeur is not None):
            serviceProfesseur = ServiceProfesseur(professeur)
            libelleGrade = input("nom du diplome : ")
            serviceProfesseur.ajouterDiplome(libelleGrade)
        print("")

    def afficherDiplome(self):

        professeurs = self.professeursDAO.findAll()
        print("")
        print("De qui voulez vous voir ses Diplomes ? ")
        for professeur in professeurs:
            print("{} : {} {} ".format(professeur.licence, professeur.prenom, professeur.nom))

        choixLicence = int(input("Tapez son numero de licence : "))
        professeur = self.professeursDAO.findById(choixLicence)
        print("")
        if (professeur is not None):
            for diplome in professeur.diplomes:
                print("{} obtenu le {}".format(diplome.libelle, diplome.dateObtention))
        print("")
