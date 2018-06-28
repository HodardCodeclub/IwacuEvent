# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528621681.656461
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingCalendar.tpl'
_template_uri = 'RoomBookingCalendar.tpl'
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
        calendar = context.get('calendar', UNDEFINED)
        max_days = context.get('max_days', UNDEFINED)
        overload = context.get('overload', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<h2 class="page-title">\n    ')
        __M_writer(str(encode_if_unicode( _('Calendar') )))
        __M_writer('\n</h2>\n\n')
        if overload:
            __M_writer('    <div class="error-message-box">\n        <div class="message-text">\n            ')
            __M_writer(str(encode_if_unicode( _('The period may not be longer than {0} days.').format(max_days) )))
            __M_writer('\n        </div>\n    </div>\n')
        __M_writer('\n')
        __M_writer(str(encode_if_unicode( calendar )))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 6, "33": 8, "34": 8, "35": 12, "36": 13, "37": 13, "43": 37, "20": 0, "28": 1, "29": 2, "30": 2, "31": 5}, "uri": "RoomBookingCalendar.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingCalendar.tpl"}
__M_END_METADATA
"""
