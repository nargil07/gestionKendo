from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine('sqlite:///bd.db', echo=False)

"""
Model Adherent representation d'un adherent
"""
class Adherent(Base):
    __tablename__ = 'Adherents'
    licence = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    prenom = Column(String(50), nullable=False)
    dateNaissance = Column(DateTime, nullable=False)
    grades = relationship("Grade")
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'Adherents',
        'polymorphic_on': type
    }

    def __init__(self, nom, prenom, dateNaissance):
        self.nom = nom
        self.prenom = prenom
        self.dateNaissance = dateNaissance

    def __str__(self):
        return ("Adherent : [Licence : {}, nom : {}, prenom : {}, dateNaissance : {}]".format(self.licence, self.nom,
                                                                                              self.prenom,
                                                                                              self.dateNaissance))


    def __repr__(self):
        return (
        "Adherent : [Licence : {}, nom : {}, prenom : {}, dateNaissance : {}]".format(self.licence, self.nom,
                                                                                      self.prenom,
                                                                                      self.dateNaissance))

"""
Model Professeur herite d'un adherent
"""
class Professeur(Adherent):
    __tablename__ = 'Professeurs'
    licence = Column(Integer, ForeignKey('Adherents.licence'), primary_key=True, autoincrement=True)
    diplomes = relationship("Diplome")

"""
Model Grade - representation d'un grade
"""
class Grade(Base):
    __tablename__ = 'Grades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    libelle = Column(String(50), nullable=False)
    dateObtention = Column(DateTime, nullable=False)
    idAdherent = Column(Integer, ForeignKey('Adherents.licence'))

    def __init__(self, libelle, idAdherent, dateObtention):
        self.libelle = libelle
        self.idAdherent = idAdherent
        self.dateObtention = dateObtention

"""
Model Diplome - representation d'un diplome
"""
class Diplome(Base):
    __tablename__ = 'Diplomes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    libelle = Column(String(50), nullable=False)
    dateObtention = Column(DateTime, nullable=False)
    idProfesseur = Column(Integer, ForeignKey('Professeurs.licence'))

    def __init__(self, libelle, idProfesseur, dateObtention):
        self.libelle = libelle
        self.idProfesseur = idProfesseur
        self.dateObtention = dateObtention


Base.metadata.create_all(engine)
