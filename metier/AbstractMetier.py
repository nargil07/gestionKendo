from abc import ABCMeta, abstractmethod


class AbstractMetier:
    """
    Classe Abstraite qui permet de gerer la liaison entre les
    classes DAO et la vue.
    Les classes qui hériterons de celle ci devrons gerer le cache
    pour eviter les appele en bdd tous le temps.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.entities = {}

    def addEntity(self, entity):
        if(self.search(self.getKey(entity)) == None):
            self.entities[self.getKey(entity)] = entity

    def addEntities(self, entities):
        for entity in entities:
            self.addEntity(entity)

    def getListEntities(self):
        return self.entities.values()

    def setListEntities(self, entities):
        self.entities.clear()
        self.addEntities(entities)

    def getKey(self, entity):
        """
        Methode a définir pour renvoyer la clé de l'entité en fonction
        du type d'objet géré par le metier
        :param entity: l'entité d'ou on vas renvoyé sa clé
        :return string: la clé
        """
        pass

    def search(self, key):
        """
        Retourne l'objet en fonction de la clé.
        Renvoie nil si l'objet n'existe pas
        :param key:
        :return:
        """
        return self.entities[key]
