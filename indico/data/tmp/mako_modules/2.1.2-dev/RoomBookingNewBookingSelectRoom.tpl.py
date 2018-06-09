# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528552328.878027
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingNewBookingSelectRoom.tpl'
_template_uri = 'RoomBookingNewBookingSelectRoom.tpl'
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
        errors = context.get('errors', UNDEFINED)
        form = context.get('form', UNDEFINED)
        _session = context.get('_session', UNDEFINED)
        max_room_capacity = context.get('max_room_capacity', UNDEFINED)
        my_rooms = context.get('my_rooms', UNDEFINED)
        ignore_userdata = context.get('ignore_userdata', UNDEFINED)
        serializable_rooms = context.get('serializable_rooms', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<h2 class="page-title">\n    ')
        __M_writer(str(encode_if_unicode( _('Book a room') )))
        __M_writer('\n</h2>\n\n<ul id="breadcrumbs" style="margin: 0px 0px 0px -15px; padding: 0; list-style: none;">\n    <li><span class="current">')
        __M_writer(str(encode_if_unicode( _('Specify Search Criteria') )))
        __M_writer('</span></li>\n    <li><span>')
        __M_writer(str(encode_if_unicode( _('Select Available Period') )))
        __M_writer('</span></li>\n    <li><span>')
        __M_writer(str(encode_if_unicode( _('Confirm Reservation') )))
        __M_writer('</span></li>\n</ul>\n\n')
        runtime._include_file(context, 'ErrorList.tpl', _template_uri, errors=errors, msg=_("There are some errors in the search criteria"))
        __M_writer('\n\n<form id="searchForm" method="POST" action="">\n    ')
        __M_writer(str(encode_if_unicode( form.csrf_token() )))
        __M_writer('\n    <input type="hidden" name="step" value="1">\n\n    <h2 class="group-title">\n        <i class="icon-location"></i>\n        ')
        __M_writer(str(encode_if_unicode( _('Rooms') )))
        __M_writer('\n    </h2>\n    <div id="roomselector"></div>\n\n    <h2 class="group-title">\n        <i class="icon-time"></i>\n        ')
        __M_writer(str(encode_if_unicode( _('Booking time & date') )))
        __M_writer('\n    </h2>\n    ')
        runtime._include_file(context, 'RoomBookingNewBookingPeriodWidget.tpl', _template_uri, form=form, flexibility=True)
        __M_writer('\n\n    <h2 class="group-title"></h2>\n    <button type="submit" class="i-button highlight">')
        __M_writer(str(encode_if_unicode( _('Continue') )))
        __M_writer('</button>\n</form>\n\n<script>\n    var userId = "rb-user-')
        __M_writer(str(encode_if_unicode( _session.user.id if _session.user else 'not-logged' )))
        __M_writer('";\n    var rbUserData = $.jStorage.get(userId, {});\n    var maxRoomCapacity = ')
        __M_writer(str(encode_if_unicode( max_room_capacity )))
        __M_writer(';\n    var rooms = ')
        __M_writer(j( serializable_rooms ))
        __M_writer(';\n    var myRooms = ')
        __M_writer(j( my_rooms ))
        __M_writer(';\n\n    $(document).ready(function() {\n        initWidgets();\n')
        if not ignore_userdata:
            __M_writer('            restoreUserData();\n')
        __M_writer("\n        function initWidgets() {\n            $('#roomselector').roomselector({\n                allowEmpty: false,\n                rooms: rooms,\n                myRooms: myRooms,\n                roomMaxCapacity: maxRoomCapacity,\n                userData: ")
        __M_writer(str(encode_if_unicode( 'rbUserData' if not ignore_userdata else {})))
        __M_writer(",\n                selectName: '")
        __M_writer(str(encode_if_unicode( form.room_ids.name )))
        __M_writer("',\n                selectedRooms: ")
        __M_writer(j( form.room_ids.data ))
        __M_writer('\n            });\n        }\n\n        function restoreUserData() {\n            if (rbUserData.startDate) {\n                var savedStartDate = moment(rbUserData.startDate).toDate();\n                if ($(\'#sDatePlace\').datepicker(\'getDate\').getTime() != savedStartDate.getTime()) {\n                    $(\'.js-default-date-warning\').hide();\n                }\n                $(\'#sDatePlace\').datepicker(\'setDate\', savedStartDate);\n            }\n            if (rbUserData.endDate) {\n                $("#eDatePlace").datepicker(\'setDate\', moment(rbUserData.endDate).toDate());\n            }\n\n            $("#finishDate").val(rbUserData.finishDate);\n            $("input[name=repeat_frequency][value=" + rbUserData.repeatFrequency + "]").prop(\'checked\', true).change();\n            $("#flexibleDates input[name=flexible_dates_range][value=" + rbUserData.flexibleDatesRange + "]").prop(\'checked\', true);\n\n            if (rbUserData.startTime && rbUserData.endTime) {\n                $(\'#timerange\').timerange(\'setStartTime\', rbUserData.startTime).timerange(\'setEndTime\', rbUserData.endTime);\n            }\n        }\n    });\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"20": 0, "32": 1, "33": 2, "34": 2, "35": 6, "36": 6, "37": 7, "38": 7, "39": 8, "40": 8, "41": 11, "42": 11, "43": 14, "44": 14, "45": 19, "46": 19, "47": 25, "48": 25, "49": 27, "50": 27, "51": 30, "52": 30, "53": 34, "54": 34, "55": 36, "56": 36, "57": 37, "58": 37, "59": 38, "60": 38, "61": 42, "62": 43, "63": 45, "64": 52, "65": 52, "66": 53, "67": 53, "68": 54, "69": 54, "75": 69}, "uri": "RoomBookingNewBookingSelectRoom.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingNewBookingSelectRoom.tpl"}
__M_END_METADATA
"""
