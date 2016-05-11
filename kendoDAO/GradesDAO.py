from kendoDAO.AbstractDAO import DAO
from models import Grade
from datetime import date


class GradesDAO(DAO):
    def findAll(self):
        grades = []
        for grade in self.session.query(Grade):
            grades.append(grade)
        return grades

    def findByIdAdherent(self, idAdherent):
        grades = []
        for grade in self.session.query(Grade).filter(Grade.idAdherent == idAdherent):
            grades.append(grade)
        return grades

    def insert(self, libelle, idAdherent):
        grade = Grade(libelle, idAdherent, date.today())
        self.session.add(grade)
        self.session.commit()

    def insertObject(self, grade):
        self.session.add(grade)
        self.session.commit()

    def findById(self, id):
        return self.session.query(Grade).filter(Grade.id == id).one_or_none()
