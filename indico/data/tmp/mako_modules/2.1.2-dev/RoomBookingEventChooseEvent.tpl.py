# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528744145.540124
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingEventChooseEvent.tpl'
_template_uri = 'RoomBookingEventChooseEvent.tpl'
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
        sessions = context.get('sessions', UNDEFINED)
        url_for = context.get('url_for', UNDEFINED)
        event = context.get('event', UNDEFINED)
        contribs = context.get('contribs', UNDEFINED)
        escape = context.get('escape', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<p>\n    ')
        __M_writer(str(encode_if_unicode( _('Booking a room through this interface allows two options:') )))
        __M_writer('\n</p>\n<ul>\n    <li>\n        ')
        __M_writer(str(encode_if_unicode( _('Book a room using your name - You may come back later on and assign the booked room to a particular event.') )))
        __M_writer('\n    </li>\n    <li>\n        ')
        __M_writer(str(encode_if_unicode( _('Book a room and assign it automatically to the event (Room and Location of the selected event will be automatically set).') )))
        __M_writer('\n    </li>\n</ul>\n<p><strong>Select event:</strong></p>\n<form action="')
        __M_writer(str(encode_if_unicode( url_for('event_mgmt.rooms_book', event) )))
        __M_writer('" method="get">\n    <ul style="margin-bottom: 20px; list-style-type: none;">\n        <li style="margin-bottom: 1em;">\n            <input type="radio" name="assign" value="nothing" id="assign-nothing" checked>\n            <label for="assign-nothing" style="font-weight: normal;"><strong>')
        __M_writer(str(encode_if_unicode( _('Just book the room without assigning it') )))
        __M_writer('</strong></label>\n        </li>\n        <li>\n            <input type="radio" name="assign" value="event" id="assign-event">\n            <label for="assign-event" style="font-weight: normal;">')
        __M_writer(str(encode_if_unicode( event.type_.title )))
        __M_writer(': <strong>')
        __M_writer(str(encode_if_unicode(escape( event.title ))))
        __M_writer('</strong></label>\n        </li>\n')
        for sess in sessions:
            __M_writer('            <li>\n                <input type="radio" name="assign" value="session-')
            __M_writer(str(encode_if_unicode( sess.id )))
            __M_writer('" id="assign-session-')
            __M_writer(str(encode_if_unicode( sess.id )))
            __M_writer('">\n                <label for="assign-session-')
            __M_writer(str(encode_if_unicode( sess.id )))
            __M_writer('" style="font-weight: normal;">Session: <strong>')
            __M_writer(str(encode_if_unicode(escape( sess.title ))))
            __M_writer('</strong></label>\n            </li>\n')
        for contrib in contribs:
            __M_writer('            <li>\n                <input type="radio" name="assign" value="contribution-')
            __M_writer(str(encode_if_unicode( contrib.id )))
            __M_writer('" id="assign-contribution-')
            __M_writer(str(encode_if_unicode( contrib.id )))
            __M_writer('">\n                <label for="assign-contribution-')
            __M_writer(str(encode_if_unicode( contrib.id )))
            __M_writer('" style="font-weight: normal;">Contribution: <strong>')
            __M_writer(str(encode_if_unicode(escape( contrib.title ))))
            __M_writer('</strong></label>\n            </li>\n')
        __M_writer('    </ul>\n    <div>\n        <input class="i-button" type="submit" value="')
        __M_writer(str(encode_if_unicode( _('Book Room') )))
        __M_writer('">\n    </div>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"20": 0, "30": 1, "31": 2, "32": 2, "33": 6, "34": 6, "35": 9, "36": 9, "37": 13, "38": 13, "39": 17, "40": 17, "41": 21, "42": 21, "43": 21, "44": 21, "45": 23, "46": 24, "47": 25, "48": 25, "49": 25, "50": 25, "51": 26, "52": 26, "53": 26, "54": 26, "55": 29, "56": 30, "57": 31, "58": 31, "59": 31, "60": 31, "61": 32, "62": 32, "63": 32, "64": 32, "65": 35, "66": 37, "67": 37, "73": 67}, "uri": "RoomBookingEventChooseEvent.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingEventChooseEvent.tpl"}
__M_END_METADATA
"""
