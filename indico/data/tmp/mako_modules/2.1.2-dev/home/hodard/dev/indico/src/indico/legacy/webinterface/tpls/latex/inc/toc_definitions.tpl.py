# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528744688.004466
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/inc/toc_definitions.tpl'
_template_uri = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/inc/toc_definitions.tpl'
_source_encoding = 'utf-8'
from indico.util.json import dumps as j
from indico.util.string import encode_if_unicode, sanitize_html
from indico.util.string import render_markdown_utf8 as m
from indico.util.i18n import _
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\\makeatletter\n\\renewcommand\\tableofcontents{%\n    \\if@twocolumn\n      \\@restonecoltrue\\onecolumn\n    \\else\n      \\@restonecolfalse\n    \\fi\n    \\chapter*{\\contentsname}%\n    \\@starttoc{toc}%\n    \\if@restonecol\\twocolumn\\fi\n}\n\\renewcommand*\\l@chapter[2]{%\n  \\ifnum \\c@tocdepth >\\m@ne\n    \\addpenalty{-\\@highpenalty}%\n    \\vskip 1.0em \\@plus\\p@\n    \\setlength\\@tempdima{1.5em}%\n    \\begingroup\n      \\parindent \\z@ \\rightskip \\@pnumwidth\n      \\parfillskip -\\@pnumwidth\n      \\leavevmode\n      \\advance\\leftskip\\@tempdima\n      \\hskip -\\leftskip\n      #1\\nobreak\n      \\xleaders\\hbox{$\\m@th\n        \\mkern \\@dotsep mu\\hbox{.}\\mkern \\@dotsep\n        mu$}\\hfill%\n      \\nobreak\\hb@xt@\\@pnumwidth{\\hss #2}\\par\n      \\penalty\\@highpenalty\n    \\endgroup\n  \\fi}\n\\makeatother')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"25": 1, "20": 0, "31": 25}, "uri": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/inc/toc_definitions.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/inc/toc_definitions.tpl"}
__M_END_METADATA
"""
