from datetime import time

from kendoDAO.AdherentsDAO import AdherentsDAO


class GestionAdherent():

    def __init__(self):
        self.adherentsDAO = AdherentsDAO()

    def afficherAdherents(self):
        adherents = self.adherentsDAO.findAll()
        print("\n")
        for adherent in adherents:
            print("{} : {} {} ".format(adherent.licence, adherent.prenom, adherent.nom))
        print("\n")

    def afficherAjoutAdherent(self):

        nom = input("Nom : ")
        prenom = input("Prenom : ")
        dateNaissance  = time.strptime(input("Date de naissance (JJ/MM/AAA) : "), "%d/%m/%Y")


    def afficherGradeAdherents(self):
        adherents = self.adherentsDAO.findAll()
        print("\n")
        print("De qui voulez vous voirs ses grades ? ")
        for adherent in adherents:
            print("{} : {} {} ".format(adherent.licence, adherent.prenom, adherent.nom))

        choixLicence = int(input("Tapez son numero de licence : "))
        adherent = self.adherentsDAO.findById(choixLicence)
        print("\n")
        if(adherent is not None):
            for grade in adherent.grades:
                print "{} obtenu le {}".format(grade.libelle, grade.dateObtention)
        print "\n"
