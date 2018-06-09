# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528552328.91166
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/ErrorList.tpl'
_template_uri = 'ErrorList.tpl'
_source_encoding = 'utf-8'
from indico.util.json import dumps as j
from indico.util.string import encode_if_unicode, sanitize_html
from indico.util.string import render_markdown_utf8 as m
from indico.util.i18n import _
_exports = []


def render_body(context,errors,msg,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(msg=msg,pageargs=pageargs,errors=errors)
        __M_writer = context.writer()
        __M_writer('\n')
        if errors:
            __M_writer('    <div class="error-message-box">\n        <div class="message-text">\n            ')
            __M_writer(str(encode_if_unicode( msg )))
            __M_writer(':\n            <ul>\n')
            for error in errors:
                __M_writer('                    <li>')
                __M_writer(str(encode_if_unicode( error )))
                __M_writer('</li>\n')
            __M_writer('            </ul>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 8, "33": 8, "34": 10, "40": 34, "20": 1, "25": 1, "26": 2, "27": 3, "28": 5, "29": 5, "30": 7, "31": 8}, "uri": "ErrorList.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/ErrorList.tpl"}
__M_END_METADATA
"""
