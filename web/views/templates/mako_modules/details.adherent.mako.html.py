# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463001383.143167
_enable_loop = True
_template_filename = '/home/antony/Documents/python/gestionKendo/web/views/templates/details.adherent.mako.html'
_template_uri = 'details.adherent.mako.html'
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
        adherent = context.get('adherent', UNDEFINED)
        def container():
            return render_container(context._locals(__M_locals))
        grades = context.get('grades', UNDEFINED)
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
        adherent = context.get('adherent', UNDEFINED)
        def container():
            return render_container(context)
        grades = context.get('grades', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div class="col-lg-12">\n        <div class="col-lg-4"></div>\n        <div class="col-lg-4">\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    Adherent\n                </div>\n                <div class="panel-body">\n                    <p>Nom : ')
        __M_writer(str(adherent.nom))
        __M_writer('</p>\n                    <p>Prenom : ')
        __M_writer(str(adherent.prenom))
        __M_writer('</p>\n                    <p>Date de naissance : ')
        __M_writer(str(adherent.dateNaissance))
        __M_writer('</p>\n                    <div class="row">\n                        <div class="col-lg-12">\n                            <div class="panel panel-default">\n                                <div class="panel-heading">\n                                    Grades\n                                    <span class="glyphicon glyphicon-plus pull-right plus-button" aria-hidden="true"\n                                          data-toggle="modal" data-target="#addGrade"></span>\n                                </div>\n                                <div class="panel-body">\n                                    <table class="col-lg-12">\n                                        <thead>\n                                        <th>Libelle</th>\n                                        <th>Date</th>\n                                        <th>Action</th>\n                                        </thead>\n                                        <tbody>\n')
        for grade in grades:
            __M_writer('                                        <tr>\n                                            <td>')
            __M_writer(str(grade.libelle))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(grade.dateObtention))
            __M_writer('</td>\n                                            <td>\n                                                <form action="supressGrade" method="post">\n                                                    <input name="licence" type="hidden" value="')
            __M_writer(str(adherent.licence))
            __M_writer('"/>\n                                                    <input name="idGrade" type="hidden" value="')
            __M_writer(str(grade.id))
            __M_writer('"/>\n                                                    <input type="submit" value="Supprimer"/>\n                                                </form>\n                                            </td>\n                                        </tr>\n')
        __M_writer('                                        </tbody>\n                                    </table>\n                                </div>\n                            </div>\n                        </div>\n                    </div>\n                </div>\n            </div>\n            <div class="col-lg-4"></div>\n        </div>\n    </div>\n</div>\n<!-- Modal Ajout grade -->\n<div class="modal fade" id="addGrade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\n    <div class="modal-dialog" role="document">\n        <div class="modal-content">\n            <form action="ajoutGradeAdherent">\n                <div class="modal-header">\n                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span\n                            aria-hidden="true">&times;</span></button>\n                    <h4 class="modal-title">Ajout d\'un grade</h4>\n                </div>\n                <div class="modal-body">\n                    <input type="hidden" name="licence" value="')
        __M_writer(str(adherent.licence))
        __M_writer('">\n                    <input type="text" name="libelle">\n                    <input type="date" name="date">\n                </div>\n                <div class="modal-footer">\n                    <input type="submit" class="btn btn-primary" value="Valider">\n                </div>\n            </form>\n        </div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/home/antony/Documents/python/gestionKendo/web/views/templates/details.adherent.mako.html", "uri": "details.adherent.mako.html", "line_map": {"64": 33, "65": 34, "66": 34, "67": 37, "68": 37, "69": 38, "70": 38, "71": 44, "72": 67, "73": 67, "79": 73, "27": 0, "36": 1, "46": 2, "54": 2, "55": 12, "56": 12, "57": 13, "58": 13, "59": 14, "60": 14, "61": 31, "62": 32, "63": 33}}
__M_END_METADATA
"""
