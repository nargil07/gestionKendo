# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1463050052.5001063
_enable_loop = True
_template_filename = '/home/antony/Documents/python/gestionKendo/web/views/templates/details.professeur.mako.html'
_template_uri = 'details.professeur.mako.html'
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
        def container():
            return render_container(context._locals(__M_locals))
        grades = context.get('grades', UNDEFINED)
        diplomes = context.get('diplomes', UNDEFINED)
        professeur = context.get('professeur', UNDEFINED)
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
        def container():
            return render_container(context)
        grades = context.get('grades', UNDEFINED)
        diplomes = context.get('diplomes', UNDEFINED)
        professeur = context.get('professeur', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div class="col-lg-12">\n        <div class="col-lg-4"></div>\n        <div class="col-lg-4">\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    Professeur\n                    <span class="glyphicon glyphicon-pencil pull-right plus-button" aria-hidden="true"\n                                          data-toggle="modal" data-target="#modifier"></span>\n                </div>\n                <div class="panel-body">\n                    <p>Nom : ')
        __M_writer(str(professeur.nom))
        __M_writer('</p>\n                    <p>Prenom : ')
        __M_writer(str(professeur.prenom))
        __M_writer('</p>\n                    <p>Date de naissance : ')
        __M_writer(str(professeur.dateNaissance))
        __M_writer('</p>\n                    <div class="row">\n                        <div class="col-lg-12">\n                            <div class="panel panel-default">\n                                <div class="panel-heading">\n                                    Grades\n                                    <span class="glyphicon glyphicon-plus pull-right plus-button" aria-hidden="true"\n                                          data-toggle="modal" data-target="#addGrade"></span>\n                                </div>\n                                <div class="panel-body">\n                                    <table class="col-lg-12">\n                                        <thead>\n                                        <th>Libelle</th>\n                                        <th>Date</th>\n                                        <th>Action</th>\n                                        </thead>\n                                        <tbody>\n')
        for grade in grades:
            __M_writer('                                        <tr>\n                                            <td>')
            __M_writer(str(grade.libelle))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(grade.dateObtention))
            __M_writer('</td>\n                                            <td>\n                                                <form action="supressGradeProf" method="post">\n                                                    <input name="licence" type="hidden" value="')
            __M_writer(str(professeur.licence))
            __M_writer('"/>\n                                                    <input name="idGrade" type="hidden" value="')
            __M_writer(str(grade.id))
            __M_writer('"/>\n                                                    <input type="submit" value="Supprimer"/>\n                                                </form>\n                                            </td>\n                                        </tr>\n')
        __M_writer('                                        </tbody>\n                                    </table>\n\n                                </div>\n                            </div>\n                        </div>\n                    </div>\n                    <div class="row">\n                        <div class="col-lg-12">\n                            <div class="panel panel-default">\n                                <div class="panel-heading">\n                                    Diplomes\n                                    <span class="glyphicon glyphicon-plus pull-right plus-button" aria-hidden="true"\n                                          data-toggle="modal" data-target="#addDiplome"></span>\n                                </div>\n                                <div class="panel-body">\n                                    <table class="col-lg-12">\n                                        <thead>\n                                        <th>Libelle</th>\n                                        <th>Date</th>\n                                        <th>Action</th>\n                                        </thead>\n                                        <tbody>\n')
        for diplome in diplomes:
            __M_writer('                                        <tr>\n                                            <td>')
            __M_writer(str(diplome.libelle))
            __M_writer('</td>\n                                            <td>')
            __M_writer(str(diplome.dateObtention))
            __M_writer('</td>\n                                            <td>\n                                                <form action="supressGradeProf" method="post">\n                                                    <input name="licence" type="hidden" value="')
            __M_writer(str(professeur.licence))
            __M_writer('"/>\n                                                    <input name="idGrade" type="hidden" value="')
            __M_writer(str(diplome.id))
            __M_writer('"/>\n                                                    <input type="submit" value="Supprimer"/>\n                                                </form>\n                                            </td>\n                                        </tr>\n')
        __M_writer('                                        </tbody>\n                                    </table>\n                                </div>\n                            </div>\n                        </div>\n                    </div>\n                </div>\n            </div>\n            <div class="col-lg-4"></div>\n        </div>\n    </div>\n</div>\n<!-- Modal Ajout Diplome -->\n<div class="modal fade" id="addDiplome" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\n    <div class="modal-dialog" role="document">\n        <div class="modal-content">\n            <form action="ajoutDiplome">\n                <div class="modal-header">\n                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span\n                            aria-hidden="true">&times;</span></button>\n                    <h4 class="modal-title">Ajout d\'un diplomes</h4>\n                </div>\n                <div class="modal-body">\n                    <input type="hidden" name="licence" value="')
        __M_writer(str(professeur.licence))
        __M_writer('">\n                    <div class="input-group">\n                        <span class="input-group-addon">Libelle</span>\n                        <input type="text" name="libelle" class="form-control" placeholder="Libelle">\n                    </div>\n                    <div class="input-group">\n                        <span class="input-group-addon">Date Obtention</span>\n                        <input type="date" name="date" class="form-control" placeholder="YYYY-MM-DD">\n                    </div>\n                </div>\n                <div class="modal-footer">\n                    <input type="submit" class="btn btn-primary" value="Valider">\n                </div>\n            </form>\n        </div>\n    </div>\n</div>\n<!-- Modal Ajout grade -->\n<div class="modal fade" id="addGrade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\n    <div class="modal-dialog" role="document">\n        <div class="modal-content">\n            <form action="ajoutGradeProf">\n                <div class="modal-header">\n                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span\n                            aria-hidden="true">&times;</span></button>\n                    <h4 class="modal-title">Ajout d\'un grade</h4>\n                </div>\n                <div class="modal-body">\n                    <input type="hidden" name="licence" value="')
        __M_writer(str(professeur.licence))
        __M_writer('">\n                    <div class="input-group">\n                        <span class="input-group-addon">Libelle</span>\n                        <input type="text" name="libelle" class="form-control" placeholder="Libelle">\n                    </div>\n                    <div class="input-group">\n                        <span class="input-group-addon">Date Obtention</span>\n                        <input type="date" name="date" class="form-control" placeholder="YYYY-MM-DD">\n                    </div>\n                </div>\n                <div class="modal-footer">\n                    <input type="submit" class="btn btn-primary" value="Valider">\n                </div>\n            </form>\n        </div>\n    </div>\n</div>\n<!-- Modal Ajout grade -->\n<div class="modal fade" id="modifier" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">\n    <div class="modal-dialog" role="document">\n        <div class="modal-content">\n            <form action="modifierProfesseur">\n                <div class="modal-header">\n                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span\n                            aria-hidden="true">&times;</span></button>\n                    <h4 class="modal-title">Modification professeur</h4>\n                </div>\n                <div class="modal-body">\n                    <input type="hidden" name="licence" value="')
        __M_writer(str(professeur.licence))
        __M_writer('">\n                    <div class="input-group">\n                        <span class="input-group-addon">Nom</span>\n                        <input type="text" name="nom" class="form-control" placeholder="Nom" value="')
        __M_writer(str(professeur.nom))
        __M_writer('">\n                    </div>\n                    <div class="input-group">\n                        <span class="input-group-addon">Prenom</span>\n                        <input type="text" name="prenom" class="form-control" placeholder="Prenom" value="')
        __M_writer(str(professeur.prenom))
        __M_writer('">\n                    </div>\n                    <div class="input-group">\n                        <span class="input-group-addon">Date Naissance</span>\n                        <input type="date" name="datenaissance" class="form-control" placeholder="YYYY-MM-DD" value="')
        __M_writer(str(professeur.dateNaissance))
        __M_writer('">\n                    </div>\n                </div>\n                <div class="modal-footer">\n                    <input type="submit" class="btn btn-primary" value="Valider">\n                </div>\n            </form>\n        </div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"27": 0, "37": 1, "47": 2, "56": 2, "57": 14, "58": 14, "59": 15, "60": 15, "61": 16, "62": 16, "63": 33, "64": 34, "65": 35, "66": 35, "67": 36, "68": 36, "69": 39, "70": 39, "71": 40, "72": 40, "73": 46, "74": 69, "75": 70, "76": 71, "77": 71, "78": 72, "79": 72, "80": 75, "81": 75, "82": 76, "83": 76, "84": 82, "85": 105, "86": 105, "87": 133, "88": 133, "89": 161, "90": 161, "91": 164, "92": 164, "93": 168, "94": 168, "95": 172, "96": 172, "102": 96}, "source_encoding": "ascii", "uri": "details.professeur.mako.html", "filename": "/home/antony/Documents/python/gestionKendo/web/views/templates/details.professeur.mako.html"}
__M_END_METADATA
"""
