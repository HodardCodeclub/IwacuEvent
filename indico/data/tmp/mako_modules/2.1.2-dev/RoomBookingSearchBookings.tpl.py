# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528572569.234705
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingSearchBookings.tpl'
_template_uri = 'RoomBookingSearchBookings.tpl'
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
        my_rooms = context.get('my_rooms', UNDEFINED)
        errors = context.get('errors', UNDEFINED)
        form = context.get('form', UNDEFINED)
        rooms = context.get('rooms', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<h2 class="page-title">\n    ')
        __M_writer(str(encode_if_unicode( _('Search bookings') )))
        __M_writer('\n</h2>\n\n')
        runtime._include_file(context, 'ErrorList.tpl', _template_uri, errors=errors, msg=_("There are some errors in the search criteria"))
        __M_writer('\n\n<form method="post" action="" id="searchBookings">\n    ')
        __M_writer(str(encode_if_unicode( form.csrf_token() if form.meta.csrf else '' )))
        __M_writer('\n    <h2 class="group-title">\n        <i class="icon-location"></i>\n        ')
        __M_writer(str(encode_if_unicode( _('Taking place in') )))
        __M_writer('\n    </h2>\n\n    <div id="roomselector"></div>\n\n    <div id="timespan">\n        <h2 class="group-title">\n            <i class="icon-time"></i>\n            ')
        __M_writer(str(encode_if_unicode( _('Timespan') )))
        __M_writer('\n        </h2>\n\n        <div class="toolbar thin space-after">\n            <div class="group with-datepicker">\n                <span class="i-button label heavy">\n                    ')
        __M_writer(str(encode_if_unicode( _('Start Date') )))
        __M_writer('\n                </span>\n                <span class="datepicker thin">\n                    <input type="text" name="start_date" id="start_date"/>\n                </span>\n            </div>\n\n            <div class="group right with-datepicker">\n                <span class="i-button label heavy">\n                    ')
        __M_writer(str(encode_if_unicode( _('End Date') )))
        __M_writer('\n                </span>\n                <span class="datepicker thin">\n                    <input type="text" name="end_date" id="end_date"/>\n                </span>\n            </div>\n        </div>\n        <div id="timerange"></div>\n    </div>\n\n    <div id="bookingDetails">\n        <h2 class="group-title">\n            <i class="icon-info"></i>\n            ')
        __M_writer(str(encode_if_unicode( _('Booking details') )))
        __M_writer('\n        </h2>\n\n        <div class="toolbar thin space-after">\n            <div class="group">\n                <span class="i-button label">\n                    ')
        __M_writer(str(encode_if_unicode( _('Booked for') )))
        __M_writer('\n                </span>\n                <input size="30" type="text" id="booked_for_name" name="booked_for_name"\n                    placeholder="')
        __M_writer(str(encode_if_unicode( _('Enter name...') )))
        __M_writer('" />\n            </div>\n        </div>\n        <div class="toolbar thin space-after">\n            <div class="group">\n                <span class="i-button label">\n                    ')
        __M_writer(str(encode_if_unicode( _('Reason') )))
        __M_writer('\n                </span>\n                <input size="30" type="text" id="reason" name="reason"\n                    placeholder="')
        __M_writer(str(encode_if_unicode( _('Enter reason...') )))
        __M_writer('"/>\n            </div>\n        </div>\n\n        <div class="toolbar thin space-after table">\n            <div class="group i-selection">\n                <span class="i-button label">\n                    ')
        __M_writer(str(encode_if_unicode( _('Booked') )))
        __M_writer('\n                </span>\n                <input type="radio" id="any_booker" name="is_only_mine" value="false" checked/>\n                <label for="any_booker" class="i-button"\n                    title="')
        __M_writer(str(encode_if_unicode( _('Shows all bookings') )))
        __M_writer('">\n                    ')
        __M_writer(str(encode_if_unicode( _('Anyone') )))
        __M_writer('\n                </label>\n                <input type="radio" id="only_mine" name="is_only_mine" value="true"/>\n                <label for="only_mine" class="i-button"\n                    title="')
        __M_writer(str(encode_if_unicode( _('Filter by your bookings') )))
        __M_writer('">\n                    ')
        __M_writer(str(encode_if_unicode( _('Me') )))
        __M_writer('\n                </label>\n            </div>\n        </div>\n\n        <div class="toolbar thin space-after table">\n            <div class="group i-selection">\n                <span class="i-button label">\n                    ')
        __M_writer(str(encode_if_unicode( _('Type') )))
        __M_writer('\n                </span>\n                <input type="checkbox" id="is_only_bookings" name="is_only_bookings"/>\n                <label for="is_only_bookings" class="i-button"\n                    title="')
        __M_writer(str(encode_if_unicode( _('Filter by confirmed bookings') )))
        __M_writer('">\n                    ')
        __M_writer(str(encode_if_unicode( _('Bookings') )))
        __M_writer('\n                </label>\n                <input type="checkbox" id="is_only_pre_bookings" name="is_only_pre_bookings"/>\n                <label for="is_only_pre_bookings" class="i-button"\n                    title="')
        __M_writer(str(encode_if_unicode( _('Filter by pre-bookings') )))
        __M_writer('">\n                    ')
        __M_writer(str(encode_if_unicode( _('Pre-Bookings') )))
        __M_writer('\n                </label>\n            </div>\n        </div>\n\n        <div class="toolbar thin space-after table">\n            <div class="group i-selection">\n                <span class="i-button label">\n                    ')
        __M_writer(str(encode_if_unicode( _('State') )))
        __M_writer('\n                </span>\n                <input type="checkbox" id="is_rejected" name="is_rejected"/>\n                <label for="is_rejected" class="i-button"\n                    title="')
        __M_writer(str(encode_if_unicode( _('Filter by rejected bookings') )))
        __M_writer('">\n                    ')
        __M_writer(str(encode_if_unicode( _('Rejected') )))
        __M_writer('\n                </label>\n                <input type="checkbox" id="is_cancelled" name="is_cancelled"/>\n                <label for="is_cancelled" class="i-button"\n                    title="')
        __M_writer(str(encode_if_unicode( _('Filter by cancelled bookings') )))
        __M_writer('">\n                    ')
        __M_writer(str(encode_if_unicode( _('Cancelled') )))
        __M_writer('\n                </label>\n                <input type="checkbox" id="is_archived" name="is_archived"/>\n                <label for="is_archived" class="i-button"\n                    title="')
        __M_writer(str(encode_if_unicode( _('Filter by archived bookings') )))
        __M_writer('">\n                    ')
        __M_writer(str(encode_if_unicode( _('Archived') )))
        __M_writer('\n                </label>\n            </div>\n        </div>\n\n        <div class="toolbar thin space-after table">\n            <div class="group i-selection">\n                <span class="i-button label">\n                    ')
        __M_writer(str(encode_if_unicode( _('Services') )))
        __M_writer('\n                </span>\n                <input type="checkbox" id="uses_vc" name="uses_vc"/>\n                <label for="uses_vc" class="i-button"\n                    title="')
        __M_writer(str(encode_if_unicode( _('Filter by bookings which will use videoconference systems') )))
        __M_writer('">\n                    ')
        __M_writer(str(encode_if_unicode( _('Videoconference') )))
        __M_writer('\n                </label>\n            </div>\n        </div>\n\n        <div class="toolbar thin table">\n            <div class="group i-selection">\n                <span class="i-button label">\n                    ')
        __M_writer(str(encode_if_unicode( _('Assistance') )))
        __M_writer('\n                </span>\n                <input type="checkbox" id="needs_vc_assistance" name="needs_vc_assistance"/>\n                <label for="needs_vc_assistance" class="i-button"\n                    title="')
        __M_writer(str(encode_if_unicode( _('Filter by bookings which requested assistance for the startup of the videoconference session') )))
        __M_writer('">\n                    ')
        __M_writer(str(encode_if_unicode( _('Videoconference') )))
        __M_writer('\n                </label>\n                <input type="checkbox" id="needs_assistance" name="needs_assistance"/>\n                <label for="needs_assistance" class="i-button"\n                    title="')
        __M_writer(str(encode_if_unicode( _('Filter by bookings which requested assistance for the startup of the meeting') )))
        __M_writer('">\n                    ')
        __M_writer(str(encode_if_unicode( _('Startup') )))
        __M_writer('\n                </label>\n            </div>\n        </div>\n    </div>\n\n    <h2 class="group-title"></h2>\n    <div class="submit-button-wrapper">\n        <button type="send" class="i-button highlight">\n            <i class="icon-search"></i>\n            <span>\n                ')
        __M_writer(str(encode_if_unicode( _('Search') )))
        __M_writer('\n            </span>\n        </button>\n    </div>\n</form>\n\n<script>\n    var rooms = ')
        __M_writer(j( [r.to_serializable('__public_exhaustive__') for r in rooms] ))
        __M_writer(';\n    var myRooms = ')
        __M_writer(j( my_rooms ))
        __M_writer(";\n\n    function adjustDates(s, e) {\n        if (s.datepicker('getDate') > e.datepicker('getDate'))\n            e.datepicker('setDate', s.datepicker('getDate'));\n    }\n\n    function initWidgets() {\n        $('#roomselector').roomselector({\n            allowEmpty: false,\n            rooms: rooms,\n            myRooms: myRooms,\n            selectName: 'room_ids',\n            simpleMode: true\n        });\n\n        $('#timerange').timerange({\n            sliderWidth: '320px'\n        });\n\n        var s = $('#start_date'), e = $('#end_date');\n        $('#start_date, #end_date').datepicker({\n            onSelect: function() {\n                adjustDates(s, e);\n                $('#searchBookings').trigger('change');\n            }\n        });\n        s.datepicker('setDate', '+0');\n        e.datepicker('setDate', '+6');\n    }\n\n    // Reads out the invalid textboxes and returns false if something is invalid.\n    // Returns true if form may be submited.\n    function forms_are_valid() {\n        // Clean up - make all textboxes white again\n        var searchForm = $('#searchBookings');\n        $(':input', searchForm).removeClass('hasError');\n\n        // Init\n        var isValid = true;\n\n        // Datepicker\n        if (!moment($('#start_date').val(), 'DD/MM/YYYY').isValid()) {\n            isValid = false;\n            $('#start_date').addClass('hasError');\n        }\n        if (!moment($('#end_date').val(), 'DD/MM/YYYY').isValid()) {\n            isValid = false;\n            $('#end_date').addClass('hasError');\n        }\n\n        // Time period\n        isValid = isValid && $('#timerange').timerange('validate');\n\n        return isValid;\n    }\n\n    $(function() {\n        initWidgets();\n\n        $('#searchBookings').delegate(':input', 'keyup change', function() {\n            forms_are_valid();\n        }).submit(function(e) {\n            if (!forms_are_valid(true)) {\n                new AlertPopup($T('Error'), $T('There are errors in the form. Please correct fields with red background.')).open();\n                e.preventDefault();\n            }\n            else if(!$('#roomselector').roomselector('validate')) {\n                new AlertPopup($T('Select room'), $T('Please select a room (or several rooms).')).open();\n                e.preventDefault();\n            }\n        });\n    });\n</script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"20": 0, "29": 1, "30": 2, "31": 2, "32": 5, "33": 5, "34": 8, "35": 8, "36": 11, "37": 11, "38": 19, "39": 19, "40": 25, "41": 25, "42": 34, "43": 34, "44": 47, "45": 47, "46": 53, "47": 53, "48": 56, "49": 56, "50": 62, "51": 62, "52": 65, "53": 65, "54": 72, "55": 72, "56": 76, "57": 76, "58": 77, "59": 77, "60": 81, "61": 81, "62": 82, "63": 82, "64": 90, "65": 90, "66": 94, "67": 94, "68": 95, "69": 95, "70": 99, "71": 99, "72": 100, "73": 100, "74": 108, "75": 108, "76": 112, "77": 112, "78": 113, "79": 113, "80": 117, "81": 117, "82": 118, "83": 118, "84": 122, "85": 122, "86": 123, "87": 123, "88": 131, "89": 131, "90": 135, "91": 135, "92": 136, "93": 136, "94": 144, "95": 144, "96": 148, "97": 148, "98": 149, "99": 149, "100": 153, "101": 153, "102": 154, "103": 154, "104": 165, "105": 165, "106": 172, "107": 172, "108": 173, "109": 173, "115": 109}, "uri": "RoomBookingSearchBookings.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingSearchBookings.tpl"}
__M_END_METADATA
"""
