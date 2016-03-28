from view.metierAdherents import MetierAdherent
from view.metierProfesseurs import MetierProfesseurs


class Menu:

    def __init__(self):
        self.metierAdherents = MetierAdherent()
        self.metierProfesseurs = MetierProfesseurs()

    def afficher(self):
        print("1 : Afficher la liste des adherents")
        print("2 : Afficher la liste des professeurs")

    def run(self):
        fini = False
        while not fini:
            self.afficher()
            choix = int(input("Votre choix ? : "))

            if choix == 1:
                self.metierAdherents.afficherAdherents()
            elif choix == 2:
                self.metierProfesseurs.afficherProfesseurs()
            else:
                fini = True


if __name__ == "__main__":
    menu = Menu()
    menu.run()