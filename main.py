from view.gestionAdherents import GestionAdherent
from view.gestionProfesseurs import GestionProfesseurs


class Menu:

    def __init__(self):
        self.gestionAdherents = GestionAdherent()
        self.gestionProfesseurs = GestionProfesseurs()

    def afficher(self):
        print("1 : Afficher la liste des adherents")
        print("2 : Afficher la liste des professeurs")
        print("3 : Afficher la liste des grades d'un adherent")
        print("4 : Ajouter un adherent")
        print("5 : Ajouter un grade a un etudiant")

    def run(self):
        fini = False
        while not fini:
            self.afficher()
            choix = int(input("Votre choix ? : "))

            if choix == 1:
                self.gestionAdherents.afficherAdherents()
            elif choix == 2:
                self.gestionProfesseurs.afficherProfesseurs()
            elif choix == 3:
                self.gestionAdherents.afficherGradeAdherents()
            elif choix == 4:
                self.gestionAdherents.afficherGradeAdherents()
            else:
                fini = True


if __name__ == "__main__":
    menu = Menu()
    menu.run()