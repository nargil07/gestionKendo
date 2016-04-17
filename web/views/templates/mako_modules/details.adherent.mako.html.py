# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1460894914.1989088
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
        def container():
            return render_container(context._locals(__M_locals))
        adherent = context.get('adherent', UNDEFINED)
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
        adherent = context.get('adherent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div class="col-lg-12">\n        <div class="col-lg-2"></div>\n        <div class="col-lg-8">\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    Adherent\n                </div>\n                <div class="panel-body">\n                    <p>Nom : ')
        __M_writer(str(adherent.nom))
        __M_writer('</p>\n                    <p>Prenom : ')
        __M_writer(str(adherent.prenom))
        __M_writer('</p>\n                    <p>Date de naissance : ')
        __M_writer(str(adherent.dateNaissance))
        __M_writer('</p>\n                </div>\n            </div>\n        </div>\n        <div class="col-lg-2"></div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/antony/Documents/python/gestionKendo/web/views/templates/details.adherent.mako.html", "source_encoding": "ascii", "uri": "details.adherent.mako.html", "line_map": {"64": 58, "35": 1, "52": 2, "53": 12, "54": 12, "55": 13, "56": 13, "57": 14, "58": 14, "27": 0, "45": 2}}
__M_END_METADATA
"""
