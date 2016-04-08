import cherrypy
from mako.template import Template

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return Template(filename='/web/views/template/base.html').render()

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())