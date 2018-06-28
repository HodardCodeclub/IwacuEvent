# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528621822.613894
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingPeriodFormOld.tpl'
_template_uri = 'RoomBookingPeriodFormOld.tpl'
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
        endDT = context.get('endDT', UNDEFINED)
        contextHelp = context.get('contextHelp', UNDEFINED)
        endT = context.get('endT', UNDEFINED)
        startT = context.get('startT', UNDEFINED)
        startDT = context.get('startDT', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<script type="text/javascript">\n\n    $(document).ready(function()\n    {\n        var startDate = IndicoUI.Widgets.Generic.dateField_sdate(false,null,[\'sDay\', \'sMonth\', \'sYear\']);\n        $E(\'sDatePlace\').set(startDate);\n\n        var endDate = IndicoUI.Widgets.Generic.dateField_edate(false,null,[\'eDay\', \'eMonth\', \'eYear\']);\n        $E(\'eDatePlace\').set(endDate);\n\n        /* In case the date changes, we need to check whether the start date is greater than the end date,\n        and if it\'s so we need to change it */\n        startDate.observe(function(value) {\n            if ( IndicoUtil.parseDate(startDate.get()) > IndicoUtil.parseDate(endDate.get()) ) {\n                endDate.set(startDate.get());\n                set_repeatition_comment();\n            }\n            updateFields();\n        });\n\n        endDate.observe(function(value) {\n            if ( IndicoUtil.parseDate(startDate.get()) > IndicoUtil.parseDate(endDate.get()) ) {\n                startDate.set(endDate.get());\n                set_repeatition_comment();\n            }\n            updateFields();\n        });\n\n        $(\'#sTime, #eTime\').on(\'change\', function() {\n            updateFields();\n        });\n\n        function updateFields() {\n            $(\'#start_dt\').val(\'{0}/{1}/{2} {3}\'.format($(\'#sDay\').val(), $(\'#sMonth\').val(), $(\'#sYear\').val(), $(\'#sTime\').val()));\n            $(\'#end_dt\').val(\'{0}/{1}/{2} {3}\'.format($(\'#eDay\').val(), $(\'#eMonth\').val(), $(\'#eYear\').val(), $(\'#eTime\').val()));\n        }\n\n')
        if startDT.day != '':
            __M_writer("            startDate.set('")
            __M_writer(str(encode_if_unicode( startDT.day )))
            __M_writer('/')
            __M_writer(str(encode_if_unicode( startDT.month )))
            __M_writer('/')
            __M_writer(str(encode_if_unicode( startDT.year )))
            __M_writer("');\n")
        __M_writer('\n')
        if endDT.day != '':
            __M_writer("            endDate.set('")
            __M_writer(str(encode_if_unicode( endDT.day )))
            __M_writer('/')
            __M_writer(str(encode_if_unicode( endDT.month )))
            __M_writer('/')
            __M_writer(str(encode_if_unicode( endDT.year )))
            __M_writer("');\n")
        __M_writer('\n        updateFields();\n     });\n</script>\n    <tr id="sdatesTR" >\n        <td class="subFieldWidth" align="right" > ')
        __M_writer(str(encode_if_unicode( _("Start Date"))))
        __M_writer('&nbsp;&nbsp;</td>\n        <td class="blacktext">\n            <span id="sDatePlace"></span>\n            <input type="hidden" value="')
        __M_writer(str(encode_if_unicode( startDT.day )))
        __M_writer('" name="sDay" id="sDay"/>\n            <input type="hidden" value="')
        __M_writer(str(encode_if_unicode( startDT.month )))
        __M_writer('" name="sMonth" id="sMonth"/>\n            <input type="hidden" value="')
        __M_writer(str(encode_if_unicode( startDT.year )))
        __M_writer('" name="sYear" id="sYear"/>\n        </td>\n      </tr>\n     <tr id="edatesTR" >\n        <td class="subFieldWidth" align="right" >')
        __M_writer(str(encode_if_unicode( _("End Date"))))
        __M_writer('&nbsp;&nbsp;</td>\n        <td>\n            <span id="eDatePlace"></span>\n            <input type="hidden" value="')
        __M_writer(str(encode_if_unicode( endDT.day )))
        __M_writer('" name="eDay" id="eDay"/>\n            <input type="hidden" value="')
        __M_writer(str(encode_if_unicode( endDT.month )))
        __M_writer('" name="eMonth" id="eMonth"/>\n            <input type="hidden" value="')
        __M_writer(str(encode_if_unicode( endDT.year )))
        __M_writer('" name="eYear" id="eYear"/>\n        </td>\n    </tr>\n    <tr id="hoursTR" >\n        <td class="subFieldWidth" align="right" >')
        __M_writer(str(encode_if_unicode( _("Hours"))))
        __M_writer('&nbsp;&nbsp;</td>\n        <td align="left" class="blacktext">\n            <input name="sTime" id="sTime" maxlength="5" size="5" type="text" value="')
        __M_writer(str(encode_if_unicode( startT )))
        __M_writer('"> &nbsp;&mdash;&nbsp;\n            <input name="eTime" id="eTime" maxlength="5" size="5" type="text" value="')
        __M_writer(str(encode_if_unicode( endT )))
        __M_writer('">\n            <span id="holidays-warning" style="color: Red; font-weight:bold;"></span>\n        </td>\n    </tr>\n    <tr id="repTypeTR" >\n        <td class="subFieldWidth" align="right" >')
        __M_writer(str(encode_if_unicode( _("Type"))))
        __M_writer('&nbsp;&nbsp;</td>\n        <td align="left" class="blacktext" >\n            <select name="repeatability" id="repeatability" onchange="set_repeatition_comment();">\n                <option value="None" selected> ')
        __M_writer(str(encode_if_unicode( _("Single day"))))
        __M_writer('</option>\n                <option value="0"> ')
        __M_writer(str(encode_if_unicode( _("Repeat daily"))))
        __M_writer('</option>\n                <option value="1"> ')
        __M_writer(str(encode_if_unicode( _("Repeat once a week"))))
        __M_writer('</option>\n                <option value="2"> ')
        __M_writer(str(encode_if_unicode( _("Repeat once every two weeks"))))
        __M_writer('</option>\n                <option value="3"> ')
        __M_writer(str(encode_if_unicode( _("Repeat once every three weeks"))))
        __M_writer('</option>\n                <option value="4"> ')
        __M_writer(str(encode_if_unicode( _("Repeat every month"))))
        __M_writer('</option>\n            </select>\n            <span id="repComment" style="margin-left: 12px"></span>\n            ')
        __M_writer(str(encode_if_unicode(contextHelp('repetitionHelp' ))))
        __M_writer('\n        </td>\n    </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"20": 1, "30": 1, "31": 39, "32": 40, "33": 40, "34": 40, "35": 40, "36": 40, "37": 40, "38": 40, "39": 42, "40": 43, "41": 44, "42": 44, "43": 44, "44": 44, "45": 44, "46": 44, "47": 44, "48": 46, "49": 51, "50": 51, "51": 54, "52": 54, "53": 55, "54": 55, "55": 56, "56": 56, "57": 60, "58": 60, "59": 63, "60": 63, "61": 64, "62": 64, "63": 65, "64": 65, "65": 69, "66": 69, "67": 71, "68": 71, "69": 72, "70": 72, "71": 77, "72": 77, "73": 80, "74": 80, "75": 81, "76": 81, "77": 82, "78": 82, "79": 83, "80": 83, "81": 84, "82": 84, "83": 85, "84": 85, "85": 88, "86": 88, "92": 86}, "uri": "RoomBookingPeriodFormOld.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingPeriodFormOld.tpl"}
__M_END_METADATA
"""
