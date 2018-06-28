# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528744687.871471
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/book_of_abstracts.tpl'
_template_uri = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/book_of_abstracts.tpl'
_source_encoding = 'utf-8'
from indico.util.json import dumps as j
from indico.util.string import encode_if_unicode, sanitize_html
from indico.util.string import render_markdown_utf8 as m
from indico.util.i18n import _
_exports = ['document_class', 'header_extra', 'first_page', 'table_of_contents', 'book_body']


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
    return runtime._inherit_from(context, 'contribution_list_boa.tpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def header_extra():
            return render_header_extra(context._locals(__M_locals))
        latex_escape = context.get('latex_escape', UNDEFINED)
        def table_of_contents():
            return render_table_of_contents(context._locals(__M_locals))
        contribs = context.get('contribs', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        def document_class():
            return render_document_class(context._locals(__M_locals))
        _session = context.get('_session', UNDEFINED)
        def first_page():
            return render_first_page(context._locals(__M_locals))
        show_ids = context.get('show_ids', UNDEFINED)
        event = context.get('event', UNDEFINED)
        def book_body():
            return render_book_body(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'document_class'):
            context['self'].document_class(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_extra'):
            context['self'].header_extra(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'first_page'):
            context['self'].first_page(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'table_of_contents'):
            context['self'].table_of_contents(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'book_body'):
            context['self'].book_body(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_document_class(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def document_class():
            return render_document_class(context)
        __M_writer = context.writer()
        __M_writer('\n    \\documentclass[a4paper, 11pt, twoside]{book} %% document type\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header_extra():
            return render_header_extra(context)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(encode_if_unicode(parent.header_extra())))
        __M_writer('\n    ')
        runtime._include_file(context, 'inc/toc_definitions.tpl', _template_uri)
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_first_page(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def first_page():
            return render_first_page(context)
        event = context.get('event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        runtime._include_file(context, 'inc/first_page.tpl', _template_uri, event=event,title=_('Book of Abstracts'),show_dates=True)
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_table_of_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def table_of_contents():
            return render_table_of_contents(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('   %% TOC\n    \\tableofcontents\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_book_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        latex_escape = context.get('latex_escape', UNDEFINED)
        contribs = context.get('contribs', UNDEFINED)
        _session = context.get('_session', UNDEFINED)
        show_ids = context.get('show_ids', UNDEFINED)
        event = context.get('event', UNDEFINED)
        def book_body():
            return render_book_body(context)
        __M_writer = context.writer()
        __M_writer('\n')
        for contrib in contribs:
            if contrib.can_access(_session.user):
                __M_writer('            \\fancyhead[L]{\\small \\rmfamily \\color{gray} \\truncateellipses{')
                __M_writer(latex_escape(str(encode_if_unicode(event.title ))))
                __M_writer('}{300pt} / ')
                __M_writer(latex_escape(str(encode_if_unicode(_("Book of Abstracts") ))))
                __M_writer('}\n            \\fancyhead[R]{}\n\n            \\phantomsection\n            \\addcontentsline{toc}{chapter}{')
                __M_writer(latex_escape(str(encode_if_unicode(contrib.title ))))
                __M_writer(' ')
                __M_writer(str(encode_if_unicode(('{0}').format(contrib.friendly_id) if show_ids else '')))
                __M_writer('\n            }\n\n            ')
                runtime._include_file(context, 'inc/contribution_condensed.tpl', _template_uri, contrib=contrib)
                __M_writer('\n            \\vspace{3em}\n\n\n            \\fancyfoot[C]{\\small \\rmfamily \\color{gray} ')
                __M_writer(str(encode_if_unicode( latex_escape(_("Page {0}"), ignore_braces=True).format(r"\thepage") )))
                __M_writer('}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"133": 16, "134": 17, "140": 21, "151": 21, "152": 22, "153": 23, "154": 24, "155": 24, "156": 24, "157": 24, "158": 24, "31": 0, "160": 28, "161": 28, "162": 28, "163": 31, "164": 31, "165": 35, "166": 35, "172": 166, "52": 1, "57": 5, "159": 28, "62": 10, "67": 14, "72": 19, "77": 38, "83": 3, "89": 3, "95": 7, "102": 7, "103": 8, "104": 8, "105": 9, "106": 9, "112": 12, "119": 12, "120": 13, "121": 13, "127": 16}, "uri": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/book_of_abstracts.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/book_of_abstracts.tpl"}
__M_END_METADATA
"""
