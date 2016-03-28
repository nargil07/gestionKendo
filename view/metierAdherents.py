from kendoDAO.AdherentsDAO import AdherentsDAO


class MetierAdherent():

    def __init__(self):
        self.adherentsDAO = AdherentsDAO()

    def afficherAdherents(self):
        adherents = self.adherentsDAO.findAll()
        for adherent in adherents:
            print("{} : {} {} ".format(adherent.licence, adherent.prenom, adherent.nom))

    pass