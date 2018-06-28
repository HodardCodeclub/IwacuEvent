# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528621822.629505
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/InlineContextHelp.tpl'
_template_uri = 'InlineContextHelp.tpl'
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
        imgSrc = context.get('imgSrc', UNDEFINED)
        helpContent = context.get('helpContent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<span class="contextHelp" title="')
        __M_writer(str(encode_if_unicode( helpContent )))
        __M_writer('">\n   <img style="padding-left:5px; vertical-align: middle;" src="')
        __M_writer(str(encode_if_unicode( imgSrc )))
        __M_writer('" />\n</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"37": 31, "20": 0, "27": 1, "28": 2, "29": 2, "30": 3, "31": 3}, "uri": "InlineContextHelp.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/InlineContextHelp.tpl"}
__M_END_METADATA
"""
