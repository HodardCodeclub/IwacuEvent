# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528621681.626304
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingCalendarWidget.tpl'
_template_uri = 'RoomBookingCalendarWidget.tpl'
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
        can_navigate = context.get('can_navigate', UNDEFINED)
        details_in_new_tab = context.get('details_in_new_tab', UNDEFINED)
        bars = context.get('bars', UNDEFINED)
        days = context.get('days', UNDEFINED)
        flexible_days = context.get('flexible_days', UNDEFINED)
        specific_room = context.get('specific_room', UNDEFINED)
        show_summary = context.get('show_summary', UNDEFINED)
        show_navbar = context.get('show_navbar', UNDEFINED)
        form_data = context.get('form_data', UNDEFINED)
        repeat_frequency = context.get('repeat_frequency', UNDEFINED)
        start_dt = context.get('start_dt', UNDEFINED)
        end_dt = context.get('end_dt', UNDEFINED)
        __M_writer = context.writer()
        if can_navigate:
            if not form_data:
                __M_writer('        <form id="room-booking-calendar-form" method="GET">\n            <input type="hidden" name="start_date" value="')
                __M_writer(str(encode_if_unicode( start_dt.date().strftime('%d/%m/%Y') )))
                __M_writer('">\n            <input type="hidden" name="end_date" value="')
                __M_writer(str(encode_if_unicode( end_dt.date().strftime('%d/%m/%Y') )))
                __M_writer('">\n        </form>\n')
            else:
                __M_writer('        <form id="room-booking-calendar-form" method="POST">\n')
                for name, values in form_data.iterlists():
                    for value in values:
                        __M_writer('                    <input type="hidden" name="')
                        __M_writer(str(encode_if_unicode( name )))
                        __M_writer('" value="')
                        __M_writer(str(encode_if_unicode( value )))
                        __M_writer('">\n')
                __M_writer('        </form>\n')
        __M_writer('\n<div id="roomBookingCal"></div>\n<script>\n    var roomBookingCalendar = new RoomBookingCalendar({\n        bars: ')
        __M_writer(j( bars ))
        __M_writer(',\n        dayAttrs: ')
        __M_writer(j( days ))
        __M_writer(',\n        firstDay: ')
        __M_writer(j( start_dt.date().strftime('%Y-%m-%d') ))
        __M_writer(',\n        lastDay: ')
        __M_writer(j( end_dt.date().strftime('%Y-%m-%d') ))
        __M_writer(',\n        specificRoom: ')
        __M_writer(j( specific_room ))
        __M_writer(',\n        repeatFrequency: ')
        __M_writer(j( repeat_frequency ))
        __M_writer(',\n        flexibleDays: ')
        __M_writer(j( flexible_days ))
        __M_writer(",\n        rejectAllLink: '',\n        openDetailsInNewTab: ")
        __M_writer(j( details_in_new_tab ))
        __M_writer(',\n        showSummary: ')
        __M_writer(j( show_summary ))
        __M_writer(',\n        showNavBar: ')
        __M_writer(j( show_navbar ))
        __M_writer(',\n        canNavigate: ')
        __M_writer(j( can_navigate ))
        __M_writer(',\n        paramFormat: ')
        __M_writer(j( ('DD/MM/YYYY' if form_data else 'YYYY-MM-DD') ))
        __M_writer("\n    });\n\n    $E('roomBookingCal').set(roomBookingCalendar.draw());\n    roomBookingCalendar.addRepeatabilityBarsHovers();\n</script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"20": 0, "37": 1, "38": 2, "39": 3, "40": 4, "41": 4, "42": 5, "43": 5, "44": 7, "45": 8, "46": 9, "47": 10, "48": 11, "49": 11, "50": 11, "51": 11, "52": 11, "53": 14, "54": 17, "55": 21, "56": 21, "57": 22, "58": 22, "59": 23, "60": 23, "61": 24, "62": 24, "63": 25, "64": 25, "65": 26, "66": 26, "67": 27, "68": 27, "69": 29, "70": 29, "71": 30, "72": 30, "73": 31, "74": 31, "75": 32, "76": 32, "77": 33, "78": 33, "84": 78}, "uri": "RoomBookingCalendarWidget.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingCalendarWidget.tpl"}
__M_END_METADATA
"""
