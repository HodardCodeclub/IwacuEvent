# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528744687.978644
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/inc/document.tpl'
_template_uri = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/inc/document.tpl'
_source_encoding = 'utf-8'
from indico.util.json import dumps as j
from indico.util.string import encode_if_unicode, sanitize_html
from indico.util.string import render_markdown_utf8 as m
from indico.util.i18n import _
_exports = ['document_class', 'geometry', 'header_extra', 'content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def document_class():
            return render_document_class(context._locals(__M_locals))
        def geometry():
            return render_geometry(context._locals(__M_locals))
        def header_extra():
            return render_header_extra(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()

        import os
        import pkg_resources
        distribution = pkg_resources.get_distribution('indico-fonts')
        font_dir = os.path.join(distribution.location, 'indico_fonts')
        # Trailing slash is necessary
        font_dir = os.path.join(font_dir, '')
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['distribution','os','pkg_resources','font_dir'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'document_class'):
            context['self'].document_class(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'geometry'):
            context['self'].geometry(**pageargs)
        

        __M_writer('\n\n\\usepackage{hyperref}\n\\usepackage{amssymb}\n\\usepackage{amsmath}\n\\usepackage{fontspec}\n\n\\usepackage[english]{babel}\n\\usepackage[final, babel]{microtype} %% texblog.net/latex-archive/layout/pdflatex-microtype/\n\n\\usepackage{float} %% improved interface for floating objects\n\\usepackage[export]{adjustbox}\n\\usepackage[usenames,dvipsnames]{xcolor} %% named colors\n\\usepackage{sectsty} %% style sections\n\\usepackage{xstring}\n\\usepackage{tcolorbox}\n\\usepackage[inline]{enumitem}\n\\usepackage[breakall]{truncate}\n\\usepackage[parfill]{parskip}\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_extra'):
            context['self'].header_extra(**pageargs)
        

        __M_writer('\n\n\n\\begin{document}\n\n')
        __M_writer('   %% set fonts\n    \\setmainfont{LinLibertine_R.otf}[\n        BoldFont = LinLibertine_RB.otf,\n        ItalicFont = LinLibertine_RI.otf,\n        BoldItalicFont = LinLibertine_RBI.otf,\n        Path = ')
        __M_writer(str(encode_if_unicode( font_dir )))
        __M_writer(']\n    \\setsansfont{LinBiolinum_R.otf}[\n        BoldFont = LinBiolinum_RB.otf,\n        ItalicFont = LinBiolinum_RI.otf,\n        Path = ')
        __M_writer(str(encode_if_unicode( font_dir )))
        __M_writer(']\n\n')
        __M_writer('   %% no indentation\n    \\setlength{\\parindent}{0cm}\n\n')
        __M_writer('   %% helper commands\n\n    \\newcommand{\\truncateellipses}[2]{\n       \\truncate{#2}{#1}\n    }\n\n')
        __M_writer('   %% remove section heading numbering\n    \\setcounter{secnumdepth}{0}\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n\\end{document}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_document_class(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def document_class():
            return render_document_class(context)
        __M_writer = context.writer()
        __M_writer('\n\\documentclass[a4paper, 15pt]{article} %% document type\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_geometry(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def geometry():
            return render_geometry(context)
        __M_writer = context.writer()
        __M_writer('\n\\usepackage[a4paper, top=1em, bottom=10em]{geometry}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header_extra():
            return render_header_extra(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"20": 0, "33": 1, "44": 8, "49": 12, "54": 16, "59": 37, "60": 42, "61": 47, "62": 47, "63": 51, "64": 51, "65": 53, "66": 56, "67": 62, "72": 66, "78": 10, "84": 10, "90": 14, "96": 14, "102": 36, "108": 36, "114": 65, "120": 65, "126": 120}, "uri": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/inc/document.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/inc/document.tpl"}
__M_END_METADATA
"""
