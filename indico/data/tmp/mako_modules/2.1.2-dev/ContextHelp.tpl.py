# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528620243.596567
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/ContextHelp.tpl'
_template_uri = 'ContextHelp.tpl'
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
        helpId = context.get('helpId', UNDEFINED)
        imgSrc = context.get('imgSrc', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<span class="contextHelp" data-src="#')
        __M_writer(str(encode_if_unicode( helpId )))
        __M_writer('">\n   <span style="color: Green; margin-left: 6px; font-size:smaller;"><img style="vertical-align:text-bottom;border: None;" src="')
        __M_writer(str(encode_if_unicode( imgSrc )))
        __M_writer('" alt="Tooltip" /></span>\n</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"37": 31, "20": 0, "27": 1, "28": 2, "29": 2, "30": 3, "31": 3}, "uri": "ContextHelp.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/ContextHelp.tpl"}
__M_END_METADATA
"""
