# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528569756.783005
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/CHBookingRepetition.tpl'
_template_uri = 'CHBookingRepetition.tpl'
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
        __M_writer('\n            <!-- Repeatition -->\n            <div id="repetitionHelp" class="tip">\n                 ')
        __M_writer(str(encode_if_unicode( _("""If you want to create repeating booking,
                just select repeating Type to what you prefer.
                System will deduce week day and week of a month if necessary,
                using start date you have provided.""") )))
        __M_writer('\n                <br />\n            </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"25": 1, "26": 4, "20": 0, "30": 7, "36": 30}, "uri": "CHBookingRepetition.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/CHBookingRepetition.tpl"}
__M_END_METADATA
"""
