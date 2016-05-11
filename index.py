# -*-coding:UTF-8 -*
import inspect
from datetime import datetime

import os
import cherrypy
from kendoDAO.ProfesseursDAO import ProfesseursDAO
from mako.lookup import TemplateLookup
from kendoDAO.AdherentsDAO import AdherentsDAO
from service.ServiceAdherent import ServiceAdherent
from service.ServiceProfesseur import ServiceProfesseur

try:
    _curdir = os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
except NameError:
    __file__ = inspect.getfile(inspect.currentframe())
    _curdir = os.path.join(os.getcwd(), os.path.dirname(os.path.abspath(__file__)))
print(_curdir)

webDir = os.path.join(_curdir, 'web')
myTemplatesDir = os.path.join(webDir, 'views/templates')
myModulesDir = os.path.join(webDir, 'views/templates/mako_modules')
mylookup = TemplateLookup(directories=[myTemplatesDir], module_directory=myModulesDir,
                          output_encoding='utf-8',
                          encoding_errors='replace')

# ------------------------------------------------------------
# Templates HTML
# ------------------------------------------------------------
_pageListAdherents = mylookup.get_template("adherents.mako.html")
_pageDetailsAdherent = mylookup.get_template("details.adherent.mako.html")
_pageListProfesseurs = mylookup.get_template("professeurs.mako.html")
_pageDetailsProfesseur = mylookup.get_template("details.professeur.mako.html")


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        gestionadherent = AdherentsDAO()
        return _pageListAdherents.render(adherents=gestionadherent.findAll())

    @cherrypy.expose
    def professeurs(self):
        gestionProfesseur = ProfesseursDAO()
        return _pageListProfesseurs.render(professeurs=gestionProfesseur.findAll())

    @cherrypy.expose
    def detailsAdherent(self, licence):
        gestionadherent = AdherentsDAO()
        serviceAdherent = ServiceAdherent(gestionadherent.findById(licence))
        return _pageDetailsAdherent.render(adherent=serviceAdherent.adherent,
                                           grades=serviceAdherent.adherent.grades)

    @cherrypy.expose
    def detailsProfesseur(self, licence):
        gestionProfesseur = ProfesseursDAO()
        serviceProfesseur = ServiceProfesseur(gestionProfesseur.findById(licence))
        return _pageDetailsProfesseur.render(professeur=serviceProfesseur.professeur,
                                             grades=serviceProfesseur.professeur.grades,
                                             diplomes=serviceProfesseur.professeur.diplomes)

    @cherrypy.expose
    def ajoutDiplome(self, licence, libelle, date):
        gestionProfesseur = ProfesseursDAO()
        serviceProfesseur = ServiceProfesseur(gestionProfesseur.findById(licence))
        serviceProfesseur.ajouterDiplomeWithAllInfo(libelle, datetime.strptime(date,"%Y-%m-%d"))
        return self.detailsProfesseur(licence)

    @cherrypy.expose
    def ajoutGradeAdherent(self, licence, libelle, date):
        gestionAdherent = AdherentsDAO()
        serviceAdherent = ServiceAdherent(gestionAdherent.findById(licence))
        serviceAdherent.ajouterGradeWithAllInfo(libelle, datetime.strptime(date, "%Y-%m-%d"))
        return self.detailsAdherent(licence)

    @cherrypy.expose
    def ajoutGradeProf(self, licence, libelle, date):
        gestionAdherent = AdherentsDAO()
        serviceAdherent = ServiceAdherent(gestionAdherent.findById(licence))
        serviceAdherent.ajouterGradeWithAllInfo(libelle, datetime.strptime(date,"%Y-%m-%d"))
        return self.detailsProfesseur(licence)

    @cherrypy.expose
    def ajoutAdherent(self, prenom, nom, datenaissance):
        gestionAdherent = AdherentsDAO()
        gestionAdherent.insert(nom, prenom, datetime.strptime(datenaissance,"%Y-%m-%d"))
        return self.index()

    @cherrypy.expose
    def ajoutProfesseur(self, prenom, nom, datenaissance):
        gestionProfesseur = ProfesseursDAO()
        gestionProfesseur.insert(nom, prenom, datetime.strptime(datenaissance,"%Y-%m-%d"))
        return self.professeurs()

    @cherrypy.expose
    def supressProfesseur(self, licence):
        gestionProfesseur = ProfesseursDAO()
        professeur = gestionProfesseur.findById(licence)
        if professeur is not None:
            gestionProfesseur.delete(professeur)
        return self.professeurs()

    @cherrypy.expose
    def supressAdherent(self, licence):
        gestionAdherent = AdherentsDAO()
        adherent = gestionAdherent.findById(licence)
        if adherent is not None:
            gestionAdherent.delete(adherent)
        return self.index()

    @cherrypy.expose
    def supressGrade(self, licence, idGrade):
        gestionAdherent = AdherentsDAO()
        serviceAdherent = ServiceAdherent(gestionAdherent.findById(licence))
        serviceAdherent.supprimerGrade(idGrade)
        return self.detailsAdherent(licence)

    @cherrypy.expose
    def supressGradeProf(self, licence, idGrade):
        gestionAdherent = AdherentsDAO()
        serviceAdherent = ServiceAdherent(gestionAdherent.findById(licence))
        serviceAdherent.supprimerGrade(idGrade)
        return self.detailsProfesseur(licence)

    @cherrypy.expose
    def supressDiplome(self, licence, idDiplome):
        gestionProfesseur = ProfesseursDAO()
        serviceProfesseur = ServiceProfesseur(gestionProfesseur.findById(licence))
        serviceProfesseur.supprimerGrade(idDiplome)
        return self.detailsProfesseur(licence)



if __name__ == '__main__':
    global_conf = {
        'global': {'autoreload.on': False,
                   'server.socket_host': '127.0.0.1',
                   'server.socket_port': 8080,
                   'server.protocol_version': 'HTTP/1.1',
                   'server.thread_pool': 5,
                   'tools.encode.encoding': "Utf-8",
                   'environment': 'production',
                   'log.error_file': 'site.log',
                   'log.screen': True}}
    cherrypy.config.update(global_conf)

    conf_appli = {'/static': {'tools.staticdir.on': True,
                              'tools.staticdir.dir': os.path.join(webDir, 'static')},
                  '/static/templates': {'tools.staticdir.on': True,
                                        'tools.staticdir.dir': myTemplatesDir},
                  '/static/tmp/mako_modules': {'tools.staticdir.on': True,
                                               'tools.staticdir.dir': myModulesDir},
                  '/static/css': {'tools.staticdir.on': True,
                                  'tools.staticdir.dir': os.path.join(webDir, 'static/css'),
                                  'tools.staticdir.content_types': {'css': 'text/css'}},
                  '/static/images': {'tools.staticdir.on': True,
                                     'tools.staticdir.dir': os.path.join(webDir, 'static/images'),
                                     'tools.staticdir.content_types': {'jpg': 'image/jpg'}},
                  '/static/fonts': {'tools.staticdir.on': True,
                                    'tools.staticdir.dir': os.path.join(webDir, 'static/fonts')},
                  '/static/js': {'tools.staticdir.on': True,
                                 'tools.staticdir.dir': os.path.join(webDir, 'static/js'),
                                 'tools.staticdir.content_types': {'js': 'application/javascript'}}}

    # Démarrer le serveur HTTP CherryPy
    cherrypy.quickstart(HelloWorld(), '/', config=conf_appli)
