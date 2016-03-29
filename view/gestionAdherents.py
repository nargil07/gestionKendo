from datetime import datetime

from kendoDAO.AdherentsDAO import AdherentsDAO
from service.ServiceAdherent import ServiceAdherent


class GestionAdherent():

    def __init__(self):
        self.adherentsDAO = AdherentsDAO()

    def afficherAdherents(self):
        adherents = self.adherentsDAO.findAll()
        print("")
        for adherent in adherents:
            print("{} : {} {} ".format(adherent.licence, adherent.prenom, adherent.nom))
        print("")

    def afficherAjoutAdherent(self):
        print("")
        nom = input("Nom : ")
        prenom = input("Prenom : ")
        dateNaissance  = datetime.strptime(input("Date de naissance (JJ/MM/AAA) : "), "%d/%m/%Y")
        print("")
        self.adherentsDAO.insert(nom, prenom, dateNaissance)


    def afficherGradeAdherents(self):
        adherents = self.adherentsDAO.findAll()
        print("")
        print("De qui voulez vous voirs ses grades ? ")
        for adherent in adherents:
            print("{} : {} {} ".format(adherent.licence, adherent.prenom, adherent.nom))

        choixLicence = int(input("Tapez son numero de licence : "))
        adherent = self.adherentsDAO.findById(choixLicence)
        print("")
        if(adherent is not None):
            for grade in adherent.grades:
                print("{} obtenu le {}".format(grade.libelle, grade.dateObtention))
        print("")

    def afficherAjoutGradeAdherents(self):
        adherents = self.adherentsDAO.findAll()
        print("")
        print("De qui voulez vous donner un grade ? ")
        for adherent in adherents:
            print("{} : {} {} ".format(adherent.licence, adherent.prenom, adherent.nom))

        choixLicence = int(input("Tapez son numero de licence : "))
        adherent = self.adherentsDAO.findById(choixLicence)
        print("")
        if (adherent is not None):
            serviceAdherent = ServiceAdherent(adherent)
            libelleGrade = input("nom du grade : ")
            serviceAdherent.ajouterGrade(libelleGrade)
        print("")
