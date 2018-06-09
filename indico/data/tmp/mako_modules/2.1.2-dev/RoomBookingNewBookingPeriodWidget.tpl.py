# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528552328.968747
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingNewBookingPeriodWidget.tpl'
_template_uri = 'RoomBookingNewBookingPeriodWidget.tpl'
_source_encoding = 'utf-8'
from indico.util.json import dumps as j
from indico.util.string import encode_if_unicode, sanitize_html
from indico.util.string import render_markdown_utf8 as m
from indico.util.i18n import _
_exports = []


def render_body(context,form=None,flexibility=False,can_override=False,min_date=None,date_changed=None,past_date=None,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(can_override=can_override,form=form,pageargs=pageargs,min_date=min_date,flexibility=flexibility,date_changed=date_changed,past_date=past_date)
        booking_limit = context.get('booking_limit', UNDEFINED)
        serializable_room = context.get('serializable_room', UNDEFINED)
        room = context.get('room', UNDEFINED)
        min = context.get('min', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        from datetime import datetime 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datetime'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!-- Slider -->\n<div id="timerange"></div>\n\n<!-- Repeatibility options -->\n<div class="toolbar thin space-before space-after">\n    <div id="repeatability" class="group i-selection">\n        <span class="i-button label">')
        __M_writer(str(encode_if_unicode( _('Frequency') )))
        __M_writer('</span>\n')
        for option in form.repeat_frequency:
            __M_writer('            ')
            __M_writer(str(encode_if_unicode( option )))
            __M_writer('\n            ')
            __M_writer(str(encode_if_unicode( option.label(class_='i-button') )))
            __M_writer('\n')
        __M_writer('    </div>\n\n')
        if flexibility:
            __M_writer('        <div id="flexibleDates" class="group i-selection">\n            <span class="i-button label">')
            __M_writer(str(encode_if_unicode( _('Flexibility') )))
            __M_writer('</span>\n')
            for option in form.flexible_dates_range:
                __M_writer('                ')
                __M_writer(str(encode_if_unicode( option )))
                __M_writer('\n                ')
                __M_writer(str(encode_if_unicode( option.label(class_='i-button') )))
                __M_writer('\n')
            __M_writer('        </div>\n')
        __M_writer('</div>\n\n<!-- Datepicker -->\n<div id="datePeriod">\n    <div id="sDatePlaceDiv" class="datepicker" style="clear: both;">\n        <div id="sDatePlaceTitle" class="datepicker-title">')
        __M_writer(str(encode_if_unicode( _('Booking date') )))
        __M_writer('</div>\n        <div id="sDatePlace"></div>\n    </div>\n    <div id="eDatePlaceDiv" class="datepicker" style="display:none;">\n        <div id=\'eDatePlaceTitle\' class=\'datepicker-title\'>')
        __M_writer(str(encode_if_unicode( _('End date') )))
        __M_writer('</div>\n        <div id="eDatePlace"></div>\n    </div>\n    <div class="datepicker-info">\n')
        if room and room.max_advance_days:
            __M_writer('            <div class="info-message-box">\n                <div class="message-text">\n                    ')
            __M_writer(str(encode_if_unicode( _('This room can only be booked {0} days in advance').format(room.max_advance_days) )))
            __M_writer('\n                </div>\n            </div>\n')
        __M_writer('        <div id="holidays-warning" class="info-message-box" style="display: none">\n            <div class="message-text"></div>\n        </div>\n')
        if past_date:
            __M_writer('            <div class="highlight-message-box js-default-date-warning">\n                <div class="message-text">\n                    ')
            __M_writer(str(encode_if_unicode(_("Looks like you were trying to book a room in the past so we moved you forward to the present.") )))
            __M_writer('\n                </div>\n            </div>\n')
        if date_changed:
            __M_writer('            <div class="highlight-message-box js-default-date-warning">\n                <div class="message-text">\n                    ')
            __M_writer(str(encode_if_unicode( _("It's late, so we selected the next day for you.") )))
            __M_writer('<br>\n                    <small> ')
            __M_writer(str(encode_if_unicode( _("You can still select today in the calendar.") )))
            __M_writer('</small>\n                </div>\n            </div>\n')
        __M_writer('        <div class="error-message-box booking-limit-warning hidden">\n            <div class="message-text">\n                ')
        __M_writer(str(encode_if_unicode(_('It is not possible to book the selected room for more than {0} days').format(booking_limit) )))
        __M_writer('\n            </div>\n        </div>\n        <div class="error-message-box booking-limit-room-warning hidden">\n            <div class="message-text"></div>\n        </div>\n    </div>\n</div>\n\n')
        __M_writer(str(encode_if_unicode( form.start_dt(type='hidden') )))
        __M_writer('\n')
        __M_writer(str(encode_if_unicode( form.end_dt(type='hidden') )))
        __M_writer('\n')
        __M_writer(str(encode_if_unicode( form.repeat_interval(type='hidden') )))
        __M_writer('\n\n<script>\n    $(document).ready(function() {\n        \'use strict\';\n\n        function checkFrequency() {\n            var frequency = $(\'#repeatability input:radio[name=repeat_frequency]:checked\').val();\n\n            if (frequency === \'0\') {\n                $(\'#sDatePlaceTitle\').text("')
        __M_writer(str(encode_if_unicode( _('Booking date') )))
        __M_writer('");\n                $(\'#eDatePlaceDiv\').hide();\n                $(\'#repeat_interval\').val(\'0\');\n            } else {\n                $(\'#sDatePlaceTitle\').text("')
        __M_writer(str(encode_if_unicode(_('Start date'))))
        __M_writer('");\n                $(\'#eDatePlaceDiv\').show();\n                $(\'#repeat_interval\').val(\'1\');\n                disableInvalidDays();\n                refreshDatePicker($(\'#eDatePlace\'));\n                selectEndDate();\n            }\n\n            $(\'#flexibleDates input:radio\').prop(\'disabled\', frequency === \'1\');\n        }\n\n        function combineDatetime() {\n            var startDate = moment($(\'#sDatePlace\').datepicker(\'getDate\')).format(\'D/MM/YYYY\');\n            var endDate = moment($(\'#eDatePlace\').datepicker(\'getDate\')).format(\'D/MM/YYYY\');\n            var startTime = $(\'#timerange\').timerange(\'getStartTime\');\n            var endTime = $(\'#timerange\').timerange(\'getEndTime\');\n\n\n            $(\'#start_dt\').val(\'{0} {1}\'.format(startDate, startTime));\n            $(\'#end_dt\').val(\'{0} {1}\'.format(endDate, endTime));\n        }\n\n        function checkHolidays() {\n            var data = {};\n            var repeat_frequency = $(\'input[name=repeat_frequency]:checked\').val();\n\n            data.start_date = moment($(\'#start_dt\').val(), \'D/MM/YYYY H:m\').format(\'YYYY-MM-D\');\n            if (repeat_frequency !== \'0\') {\n                data.end_date = moment($(\'#end_dt\').val(), \'D/MM/YYYY H:m\').format(\'YYYY-MM-D\')\n            } else {\n                data.end_date = data.start_date;\n            }\n\n            var holidaysWarning = indicoSource(\'roomBooking.getDateWarning\', data);\n            holidaysWarning.state.observe(function(state) {\n                if (state == SourceState.Loaded) {\n                    var msg = holidaysWarning.get();\n                    $(\'#holidays-warning .message-text\').html(msg);\n                    $(\'#holidays-warning\').toggle(!!msg);\n                }\n            });\n        }\n\n        function disableInvalidDays() {\n            var startDate = $(\'#sDatePlace\').datepicker(\'getDate\');\n            var endMonth = +$(\'#eDatePlace .ui-datepicker-month\').val();\n            var endYear = +$(\'#eDatePlace .ui-datepicker-year\').val();\n            // Create a date on the first of the month, two months after the endMonth, endYear values.\n            var endDate = new Date(endMonth > 9 ? endYear + 1 : endYear, (endMonth + 2) % 12, 1);\n            var frequency = $(\'#repeatability input:radio[name=repeat_frequency]:checked\').val();\n\n            validEndDates = generateValidEndDates(startDate, endDate, frequencies[frequency]);\n        }\n\n        function selectEndDate() {\n            var repetition = {};\n            repetition[RRule.DAILY] = \'days\';\n            repetition[RRule.WEEKLY] = \'weeks\';\n            repetition[RRule.MONTHLY] = \'months\';\n\n            var startDate = $(\'#sDatePlace\').datepicker(\'getDate\');\n            var selectedEndDate = $(\'#eDatePlace\').datepicker(\'getDate\');\n            var frequency = frequencies[$(\'#repeatability input:radio[name=repeat_frequency]:checked\').val()];\n            var forceSetEndDate = false;\n            var endDate;\n\n            if (selectedEndDate.getTime() <= startDate.getTime()) {\n                endDate = moment(startDate).add(2, repetition[frequency]).toDate();\n                forceSetEndDate = true;\n            } else {\n                endDate = moment(selectedEndDate).add(1, repetition[frequency]).toDate();\n            }\n            var endDates = generateValidEndDates(startDate, endDate, frequency);\n\n            if (endDates !== null && endDates.length &&\n                    (forceSetEndDate || endDates.indexOf(selectedEndDate.getTime()) === -1)) {\n                $(\'#eDatePlace\').datepicker(\'setDate\', getClosestDate(endDates, selectedEndDate));\n                refreshDatePicker($(\'#eDatePlace\'));\n            }\n        }\n\n        function commonOnSelect() {\n            $(\'.js-default-date-warning\').fadeOut();\n            combineDatetime();\n            checkHolidays();\n            validateForm();\n        }\n\n        function getClosestDate(dates, date) {\n            // dates must be a sorted array of int which represent value in ms\n            // date is a date or a date in ms\n            if (date instanceof Date) {\n                date = date.getTime();\n            }\n\n            var min = 0, max = dates.length - 1;\n            var lo = 0, hi = dates.length - 1, mid = null;\n            while (lo <= hi) {\n                mid = Math.floor((lo + hi) / 2);\n                if (date < dates[mid]) {\n                    hi = mid - 1;\n                } else if (date > dates[mid]) {\n                    lo = mid + 1;\n                } else {\n                    return new Date(dates[mid]);\n                }\n            }\n\n            // Check for invalid indexes\n            if (hi < 0 && lo <= dates.length - 1) {\n                return new Date(dates[lo]);\n            } else if (lo > dates.length - 1 && hi >= 0) {\n                return new Date(dates[hi]);\n            }\n\n            var dLo = Math.abs(date - dates[lo]);\n            var dHi = Math.abs(date - dates[hi]);\n            return dLo <= dHi ? new Date(dates[lo]) : new Date(dates[hi]);\n        }\n\n        function refreshDatePicker($dpElem) {\n            var disabled = $dpElem.datepicker(\'isDisabled\');\n            $dpElem.datepicker(\'refresh\');\n            if (disabled) {\n                $dpElem.datepicker(\'disable\');\n            }\n        }\n\n        function checkBookingLimit() {\n            var oneDay = 86400 * 1000;\n            var startDate = $(\'#sDatePlace\').datepicker(\'getDate\');\n            var endDate = $(\'#eDatePlace\').datepicker(\'getDate\');\n            var selectedDaysPeriod = (endDate - startDate) / oneDay;\n            var selectedRooms;\n')
        if serializable_room:
            __M_writer('                // Individual booking\n                selectedRooms = [')
            __M_writer(j( serializable_room ))
            __M_writer('];\n')
        else:
            __M_writer('                // Multiple select booking\n                var selectedRoomsIndexes = $("#roomselector").roomselector("selection");\n                selectedRooms = _.map(selectedRoomsIndexes, function(i) { return rooms[i]; });\n')
        __M_writer('            var selectedNotLimitedRooms = _.clone(selectedRooms);\n            var limitedRoomsInvalid = [];\n            _.each(selectedRooms, function(room) {\n                var roomBookingLimit = room.booking_limit_days;\n                if (roomBookingLimit) {\n                    selectedNotLimitedRooms.splice(selectedNotLimitedRooms.indexOf(room), 1);\n                    if (selectedDaysPeriod > roomBookingLimit) {\n                        limitedRoomsInvalid.push(room);\n                    }\n                }\n            });\n            handleLimitedRoomsInvalid(limitedRoomsInvalid);\n            if (selectedNotLimitedRooms.length) {\n                var bookingDaysLimit = ')
        __M_writer(str(encode_if_unicode( booking_limit )))
        __M_writer(';\n                var isLimitExceeded = endDate > startDate && selectedDaysPeriod > bookingDaysLimit;\n                $(\'.booking-limit-warning\').toggleClass(\'hidden\', !isLimitExceeded);\n                $(\'#searchForm :submit, #bookingForm :submit\').prop(\'disabled\', isLimitExceeded);\n            } else {\n                $(\'.booking-limit-warning\').addClass(\'hidden\');\n                $(\'#searchForm :submit, #bookingForm :submit\').prop(\'disabled\', !!limitedRoomsInvalid.length);\n            }\n        }\n\n        function handleLimitedRoomsInvalid(rooms) {\n            if (rooms.length) {\n                var warningMsgRooms = [];\n                _.map(rooms, function(room) {\n                    warningMsgRooms.push("\'{0}\' for more than {1} days".format(room.name, room.booking_limit_days));\n                });\n                var warningMsg = $T.gettext("It is not possible to book room {0}").format(warningMsgRooms.join(", "));\n                $(\'.booking-limit-room-warning .message-text\').html(warningMsg);\n            }\n            $(\'.booking-limit-room-warning\').toggleClass(\'hidden\', !rooms.length);\n        }\n\n        var validEndDates = null;\n        var frequencies = {\n            \'1\' : RRule.DAILY,\n            \'2\' : RRule.WEEKLY,\n            \'3\' : RRule.MONTHLY\n        };\n\n        $(\'#timerange\').timerange({\n            initStartTime: \'')
        __M_writer(str(encode_if_unicode( form.start_dt.data.strftime("%H:%M") )))
        __M_writer("',\n            initEndTime: '")
        __M_writer(str(encode_if_unicode( form.end_dt.data.strftime("%H:%M") )))
        __M_writer("',\n            startTimeName: 'sTime',\n            endTimeName: 'eTime',\n            sliderWidth: '512px',\n            change: function() {\n                combineDatetime();\n                validateForm();\n            }\n        });\n\n        $('#sDatePlace, #eDatePlace').datepicker({\n            dateformat: 'dd/mm/yy',\n")
        if not can_override:
            __M_writer('                maxDate: ')
            __M_writer(str(encode_if_unicode( room.max_advance_days - 1 if room and room.max_advance_days else 'null' )))
            __M_writer(',\n')
        __M_writer("            showButtonPanel: true,\n            changeMonth: true,\n            changeYear: true,\n            showOn: 'focus',\n            unifyNumRows: true\n        });\n\n")
        if not can_override:
            __M_writer("            $('#sDatePlace').datepicker('option', 'minDate', ")
            __M_writer(str(encode_if_unicode( "'{}'".format(min(min_date, form.start_dt.data).strftime('%d/%m/%Y')) if min_date else 0 )))
            __M_writer(");\n            $('#eDatePlace').datepicker('option', 'minDate', ")
            __M_writer(str(encode_if_unicode( "'{}'".format(min_date.strftime('%d/%m/%Y')) if min_date else 0 )))
            __M_writer(');\n')
        __M_writer('\n        $(\'#eDatePlace\').datepicker(\'option\', \'beforeShowDay\', function validateDate(date) {\n            if (validEndDates === null) {\n                return [true, \'\', \'\'];\n            }\n            return [validEndDates.indexOf(date.getTime()) !== -1, \'\', \'\'];\n        });\n\n        $(\'#sDatePlace\').datepicker(\'option\', \'onSelect\', function startDateOnSelect(selectedDateText) {\n            disableInvalidDays();\n            refreshDatePicker($(\'#eDatePlace\'));\n            selectEndDate();\n            commonOnSelect();\n            checkBookingLimit();\n        });\n\n        $(\'#eDatePlace\').datepicker(\'option\', \'onSelect\', function() {\n            commonOnSelect();\n            checkBookingLimit();\n        });\n\n        $(\'#eDatePlace\').datepicker(\'option\', \'onChangeMonthYear\', disableInvalidDays);\n\n        $(\'#sDatePlace\').datepicker(\'setDate\', "')
        __M_writer(str(encode_if_unicode( form.start_dt.data.strftime('%d/%m/%Y') )))
        __M_writer('");\n        $(\'#eDatePlace\').datepicker(\'setDate\', "')
        __M_writer(str(encode_if_unicode( form.end_dt.data.strftime('%d/%m/%Y') )))
        __M_writer('");\n\n        $(\'#repeatability input:radio[name=repeat_frequency]\').change(function() {\n            checkFrequency();\n        });\n\n        $(\'#roomselector\').on(\'click\', \'.ui-multiselect-checkboxes :checkbox, .ui-multiselect-all, .ui-multiselect-none\', function() {\n            checkBookingLimit();\n        });\n\n        checkFrequency();\n        checkHolidays();\n\n')
        if not can_override:
            if form.start_dt.data < datetime.now():
                __M_writer("                $('#timerange').timerange('disable');\n                var startDate = moment($('#sDatePlace').datepicker('getDate')).format('D/MM/YYYY');\n                // Disable the datea in calendar as well as the calendar itself...\n                $('#sDatePlace').datepicker('option', 'beforeShowDay', function validateDate(date) {\n                    return [moment(date).format('D/MM/YYYY') == startDate, '', ''];\n                });\n                $('#sDatePlace').datepicker('disable');\n")
            if form.end_dt.data < datetime.now():
                __M_writer("                var endDate = moment($('#eDatePlace').datepicker('getDate')).format('D/MM/YYYY');\n                // Disable the datea in calendar as well as the calendar itself...\n                $('#eDatePlace').datepicker('option', 'beforeShowDay', function validateDate(date) {\n                    return [moment(date).format('D/MM/YYYY') == endDate, '', ''];\n                });\n                $('#eDatePlace').datepicker('disable');\n                $('#repeatability > input[name=repeat_frequency]').not(':checked').prop('disabled', true);\n")
        __M_writer('\n    });\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"20": 1, "29": 1, "30": 2, "34": 2, "35": 10, "36": 10, "37": 11, "38": 12, "39": 12, "40": 12, "41": 13, "42": 13, "43": 15, "44": 17, "45": 18, "46": 19, "47": 19, "48": 20, "49": 21, "50": 21, "51": 21, "52": 22, "53": 22, "54": 24, "55": 26, "56": 31, "57": 31, "58": 35, "59": 35, "60": 39, "61": 40, "62": 42, "63": 42, "64": 46, "65": 49, "66": 50, "67": 52, "68": 52, "69": 56, "70": 57, "71": 59, "72": 59, "73": 60, "74": 60, "75": 64, "76": 66, "77": 66, "78": 75, "79": 75, "80": 76, "81": 76, "82": 77, "83": 77, "84": 87, "85": 87, "86": 91, "87": 91, "88": 225, "89": 226, "90": 227, "91": 227, "92": 228, "93": 229, "94": 233, "95": 246, "96": 246, "97": 276, "98": 276, "99": 277, "100": 277, "101": 289, "102": 290, "103": 290, "104": 290, "105": 292, "106": 299, "107": 300, "108": 300, "109": 300, "110": 301, "111": 301, "112": 303, "113": 326, "114": 326, "115": 327, "116": 327, "117": 340, "118": 341, "119": 342, "120": 350, "121": 351, "122": 360, "128": 122}, "uri": "RoomBookingNewBookingPeriodWidget.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingNewBookingPeriodWidget.tpl"}
__M_END_METADATA
"""
