# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528744687.933921
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/contribution_list_boa.tpl'
_template_uri = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/contribution_list_boa.tpl'
_source_encoding = 'utf-8'
from indico.util.json import dumps as j
from indico.util.string import encode_if_unicode, sanitize_html
from indico.util.string import render_markdown_utf8 as m
from indico.util.i18n import _
_exports = ['header_extra', 'table_of_contents', 'document_class', 'content', 'first_page', 'book_body']


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
    return runtime._inherit_from(context, 'inc/document.tpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def header_extra():
            return render_header_extra(context._locals(__M_locals))
        latex_escape = context.get('latex_escape', UNDEFINED)
        boa_text = context.get('boa_text', UNDEFINED)
        contribs = context.get('contribs', UNDEFINED)
        def document_class():
            return render_document_class(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        md_convert = context.get('md_convert', UNDEFINED)
        def first_page():
            return render_first_page(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def table_of_contents():
            return render_table_of_contents(context._locals(__M_locals))
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
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header_extra():
            return render_header_extra(context)
        __M_writer = context.writer()
        __M_writer('\n    \\usepackage{fancyhdr} %% headers\n\n    \\setlength{\\headheight}{60pt}\n    \\pagestyle{fancy}\n    \\renewcommand{\\headrulewidth}{0pt}\n\n    \\newenvironment{boa_text}\n    {\n       \\cleardoublepage\n       \\thispagestyle{empty}\n       \\vspace*{\\stretch{1}}\n       \\begin{minipage}[t]{0.66\\textwidth}\n    }%\n    {\n       \\end{minipage}\n       \\vspace*{\\stretch{3}}\n       \\clearpage\n    }\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_table_of_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def table_of_contents():
            return render_table_of_contents(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_document_class(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def document_class():
            return render_document_class(context)
        __M_writer = context.writer()
        __M_writer('\n    \\documentclass[a4paper, 11pt, oneside]{book} %% document type\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        latex_escape = context.get('latex_escape', UNDEFINED)
        def table_of_contents():
            return render_table_of_contents(context)
        contribs = context.get('contribs', UNDEFINED)
        def content():
            return render_content(context)
        md_convert = context.get('md_convert', UNDEFINED)
        def first_page():
            return render_first_page(context)
        user = context.get('user', UNDEFINED)
        boa_text = context.get('boa_text', UNDEFINED)
        event = context.get('event', UNDEFINED)
        def book_body():
            return render_book_body(context)
        __M_writer = context.writer()
        __M_writer('\n    \\setcounter{tocdepth}{0} %% remove table of contents numbering\n\n')
        __M_writer('   %% first page\n    \\frontmatter\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'first_page'):
            context['self'].first_page(**pageargs)
        

        __M_writer('\n\n')
        if boa_text:
            __M_writer('        \\begin{boa_text}\n            \\thispagestyle{fancy}\n            \\fancyhead{}\n            \\vspace{1em}\n            \\normalsize {\n                \\rmfamily {\n                    ')
            __M_writer(str(encode_if_unicode(md_convert(boa_text))))
            __M_writer('\n                }\n            }\n            \\fancyfoot[C]{\\thepage}\n        \\end{boa_text}\n')
        __M_writer('\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'table_of_contents'):
            context['self'].table_of_contents(**pageargs)
        

        __M_writer('\n\n')
        __M_writer('   %% body\n    \\mainmatter\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'book_body'):
            context['self'].book_body(**pageargs)
        

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
        __M_writer('\n        ')
        runtime._include_file(context, 'inc/first_page.tpl', _template_uri, event=event,title=_('Report of Abstracts'),show_dates=True)
        __M_writer('\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_book_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        event = context.get('event', UNDEFINED)
        latex_escape = context.get('latex_escape', UNDEFINED)
        user = context.get('user', UNDEFINED)
        contribs = context.get('contribs', UNDEFINED)
        def book_body():
            return render_book_body(context)
        __M_writer = context.writer()
        __M_writer('\n')
        for contrib in contribs:
            if contrib.can_access(user):
                __M_writer('                \\fancyhead[L]{\\small \\rmfamily \\color{gray} \\truncateellipses{')
                __M_writer(latex_escape(str(encode_if_unicode(event.title ))))
                __M_writer('}{300pt} / ')
                __M_writer(latex_escape(str(encode_if_unicode(_("Report of Abstracts") ))))
                __M_writer('}\n                \\phantomsection\n                \\addcontentsline{toc}{chapter}{')
                __M_writer(latex_escape(str(encode_if_unicode(contrib.title ))))
                __M_writer('}\n\n                \\vspace{3em}\n                ')
                runtime._include_file(context, 'inc/contribution_condensed.tpl', _template_uri, contrib=contrib)
                __M_writer('\n\n                \\fancyfoot[C]{\\small \\rmfamily \\color{gray} ')
                __M_writer(str(encode_if_unicode( latex_escape(_("Page {0}"), ignore_braces=True).format(r"\thepage") )))
                __M_writer('}\n')
        __M_writer('    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"129": 29, "130": 32, "135": 36, "136": 38, "137": 39, "138": 45, "139": 45, "140": 51, "145": 53, "146": 55, "151": 70, "157": 34, "31": 0, "164": 34, "165": 35, "166": 35, "172": 57, "192": 65, "54": 1, "183": 58, "184": 59, "185": 60, "186": 60, "59": 5, "188": 60, "189": 60, "190": 62, "191": 62, "64": 27, "193": 65, "194": 67, "195": 67, "196": 70, "69": 71, "202": 196, "75": 7, "81": 7, "87": 52, "93": 52, "182": 57, "99": 3, "105": 3, "111": 29, "187": 60}, "uri": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/contribution_list_boa.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/contribution_list_boa.tpl"}
__M_END_METADATA
"""
