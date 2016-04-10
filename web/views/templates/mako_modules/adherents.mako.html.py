# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1460304692.8684814
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
        def container():
            return render_container(context._locals(__M_locals))
        adherents = context.get('adherents', UNDEFINED)
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
        adherents = context.get('adherents', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div class="col-lg-12">\n        <div class="col-lg-2"></div>\n        <div class="col-lg-8">\n            <div class="panel panel-default">\n                <div class="panel-heading">\n                    Les adherents\n                </div>\n                <div class="panel-body">\n                    <div class="row">\n                        <table>\n')
        for adherent in adherents:
            __M_writer('                            <tr>\n                                <td>')
            __M_writer(str(adherent.nom))
            __M_writer('</td>\n                                <td>')
            __M_writer(str(adherent.prenom))
            __M_writer('</td>\n                                <td>')
            __M_writer(str(adherent.dateNaissance))
            __M_writer('</td>\n                            </tr>\n')
        __M_writer('                        </table>\n                    </div>\n                </div>\n            </div>\n        </div>\n        <div class="col-lg-2"></div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "adherents.mako.html", "filename": "/home/antony/Documents/python/gestionKendo/web/views/templates/adherents.mako.html", "source_encoding": "ascii", "line_map": {"35": 1, "45": 2, "27": 0, "67": 61, "52": 2, "53": 14, "54": 15, "55": 16, "56": 16, "57": 17, "58": 17, "59": 18, "60": 18, "61": 21}}
__M_END_METADATA
"""
