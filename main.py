# -*-coding:UTF-8 -*

from view.gestionAdherents import GestionAdherent
from view.gestionProfesseurs import GestionProfesseurs


class Menu:

    def __init__(self):
        self.gestionAdherents = GestionAdherent()
        self.gestionProfesseurs = GestionProfesseurs()

    def afficher(self):
        print("0 : Quitter l'application")
        print("1 : Afficher la liste des adherents")
        print("2 : Afficher la liste des professeurs")
        print("3 : Afficher la liste des grades d'un adherent")
        print("4 : Afficher la liste des diplomes d'un professeur")
        print("5 : Ajouter un adherent")
        print("6 : Ajouter un professeur")
        print("7 : Ajouter un grade à un adherent")
        print("8 : Ajouter un diplome à un professeur")

    def run(self):
        fini = False
        while not fini:
            self.afficher()
            try:

                choix = int(input("Votre choix ? : "))

                if choix == 1:
                    self.gestionAdherents.afficherAdherents()
                elif choix == 2:
                    self.gestionProfesseurs.afficherProfesseurs()
                elif choix == 3:
                    self.gestionAdherents.afficherGradeAdherents()
                elif choix == 4:
                    self.gestionProfesseurs.afficherDiplome()
                elif choix == 5:
                    self.gestionAdherents.afficherAjoutAdherent()
                elif choix == 6:
                    self.gestionProfesseurs.afficherAjoutProfesseur()
                elif choix == 7:
                    self.gestionAdherents.afficherAjoutGradeAdherents()
                elif choix == 8:
                    self.gestionProfesseurs.afficherAjoutDiplome()
                else:
                    fini = True
            except ValueError as valueError:
                print("Mauvais choix ....")
                print("")
            except KeyboardInterrupt:
                try:
                    print("")
                    input("Faites ctrl + c une deuxieme fois pour quitter.")
                except KeyboardInterrupt:
                    fini = True

        print("")
        print("Merci d'avoir utiliser mon logiciel.")



if __name__ == "__main__":
    menu = Menu()
    menu.run()