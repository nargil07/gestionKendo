from kendoDAO.AdherentsDAO import AdherentsDAO
from metier.AbstractMetier import AbstractMetier
from models import Adherent


class MetierAdherent(AbstractMetier):

    def __init__(self):
        AbstractMetier.__init__(self)
        self.adherentDAO = AdherentsDAO()

    def getKey(self, entity):
        """
        Renvoie la licence de l'adherent
        :param entity: Adherent
        :return:
        """
        if isinstance(entity, Adherent):
            return entity.licence
        else:
            return None

    def findAll(self):
        test = self.adherentDAO.findAll()
        print(test)
        self.setListEntities()
        return self.getListEntities()
