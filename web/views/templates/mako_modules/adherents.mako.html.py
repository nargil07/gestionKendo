# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1462975314.8661911
_enable_loop = True
_template_filename = '/home/antony/Documents/python/gestionKendo/web/views/templates/adherents.mako.html'
_template_uri = 'adherents.mako.html'
_source_encoding = 'ascii'
_exports = ['container']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.mako.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        adherents = context.get('adherents', UNDEFINED)
        def container():
            return render_container(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'container'):
            context['self'].container(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_container(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        adherents = context.get('adherents', UNDEFINED)
        def container():
            return render_container(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div class="col-lg-12">\n        <div class="col-lg-3"></div>\n        <div class="col-lg-6">\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    Les adherents\n                    <span class="glyphicon glyphicon-plus pull-right plus-button" aria-hidden="true"\n                          data-toggle="modal" data-target="#addAdherent"></span>\n                </div>\n                <div class="panel-body">\n                    <table class="col-lg-12">\n                        <thead>\n                        <th>Nom</th>\n                        <th>Prenom</th>\n                        <th>Date de naissance</th>\n                        <th>Action</th>\n                        </thead>\n                        <tbody>\n')
        for adherent in adherents:
            __M_writer('                        <tr>\n\n                            <td>')
            __M_writer(str(adherent.nom))
            __M_writer('</td>\n                            <td>')
            __M_writer(str(adherent.prenom))
            __M_writer('</td>\n                            <td>')
            __M_writer(str(adherent.dateNaissance))
            __M_writer('</td>\n                            <td>\n                                <form action="detailsAdherent">\n                                    <input type="hidden" name="licence" value="')
            __M_writer(str(adherent.licence))
            __M_writer('">\n                                    <input type="submit" value="Afficher detail">\n                                </form>\n                                <form action="supressAdherent" method="delete">\n                                    <input type="hidden" name="licence" value="')
            __M_writer(str(adherent.licence))
            __M_writer('">\n                                    <input type="submit" value="Supprimer">\n                                </form>\n                            </td>\n\n                        </tr>\n')
        __M_writer('                        </tbody>\n\n                    </table>\n                </div>\n            </div>\n        </div>\n        <div class="col-lg-3"></div>\n    </div>\n</div>\n<!-- Modal Ajout grade -->\n<div class="modal fade" id="addAdherent" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\n    <div class="modal-dialog" role="document">\n        <div class="modal-content">\n            <form action="ajoutAdherent">\n                <div class="modal-header">\n                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span\n                            aria-hidden="true">&times;</span></button>\n                    <h4 class="modal-title">Ajout d\'un grade</h4>\n                </div>\n                <div class="modal-body">\n                    <input type="text" name="prenom">\n                    <input type="text" name="nom">\n                    <input type="date" name="datenaissance">\n                </div>\n                <div class="modal-footer">\n                    <input type="submit" class="btn btn-primary" value="Valider">\n                </div>\n            </form>\n        </div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 34, "65": 41, "35": 1, "71": 65, "45": 2, "27": 0, "52": 2, "53": 22, "54": 23, "55": 25, "56": 25, "57": 26, "58": 26, "59": 27, "60": 27, "61": 30, "62": 30, "63": 34}, "uri": "adherents.mako.html", "filename": "/home/antony/Documents/python/gestionKendo/web/views/templates/adherents.mako.html"}
__M_END_METADATA
"""
