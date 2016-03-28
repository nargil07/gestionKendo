from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime,create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine('sqlite:///bd.db', echo=True)
class Adherent(Base):
    __tablename__ = 'Adherents'
    licence = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)
    dateNaissance = Column(DateTime, nullable=False)
    grades = relationship("Grade")
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity' : 'Adherents',
        'polymorphic_on' : type
    }

    def __init__(self, licence, nom, prenom, dateNaissance):
        self.nom = nom
        self.prenom = prenom
        self.licence = licence
        self.dateNaissance = dateNaissance

    def __str__(self):
        return ("Adherent : [Licence : {}, nom : {}, prenom : {}, dateNaissance : {}]".format(self.licence, self.nom, self.prenom, self.dateNaissance))

class Professeur(Adherent):
    __tablename__ = 'Professeurs'
    licence = Column(Integer, ForeignKey('Adherents.licence'), primary_key=True)
    diplomes = relationship("Diplome")

class Grade(Base):
    __tablename__ = 'Grades'
    id = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False)
    idAdherent = Column(Integer, ForeignKey('Adherents.licence'))


class Diplome(Base):
    __tablename__ = 'Diplomes'
    id = Column(Integer, primary_key=True)
    libelle = Column(String(50), nullable=False)
    idProfesseur = Column(Integer, ForeignKey('Professeurs.licence'))

Base.metadata.create_all(engine)