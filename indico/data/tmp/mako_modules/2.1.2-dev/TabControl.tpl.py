# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528744145.58783
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/TabControl.tpl'
_template_uri = 'TabControl.tpl'
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
        tabs = context.get('tabs', UNDEFINED)
        body = context.get('body', UNDEFINED)
        activeTab = context.get('activeTab', UNDEFINED)
        tabControlId = context.get('tabControlId', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<div class="static-tabs" style="display:table; width:100%;" data-active="')
        __M_writer(str(encode_if_unicode(activeTab)))
        __M_writer('">\n    <ul>\n')
        for i, (label, link, active, className) in enumerate(tabs):
            __M_writer('            <li><a href="')
            __M_writer(str(encode_if_unicode(('#static-tabs-%s-content' % tabControlId) if active else link)))
            __M_writer('" ')
            __M_writer(str(encode_if_unicode('class='+className if className else '')))
            __M_writer(' data-href="')
            __M_writer(str(encode_if_unicode(link)))
            __M_writer('">')
            __M_writer(str(encode_if_unicode(label)))
            __M_writer('</a></li>\n')
        __M_writer('    </ul>\n\n    <div id="static-tabs-')
        __M_writer(str(encode_if_unicode(tabControlId)))
        __M_writer('-content">\n        ')
        __M_writer(str(encode_if_unicode( body )))
        __M_writer('\n    </div>\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 1, "33": 3, "34": 4, "35": 4, "36": 4, "37": 4, "38": 4, "39": 4, "40": 4, "41": 4, "42": 4, "43": 6, "44": 8, "45": 8, "46": 9, "47": 9, "20": 0, "53": 47, "30": 1, "31": 1}, "uri": "TabControl.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/TabControl.tpl"}
__M_END_METADATA
"""
