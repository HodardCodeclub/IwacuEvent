# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528569756.767912
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingAdmin.tpl'
_template_uri = 'RoomBookingAdmin.tpl'
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
        contextHelp = context.get('contextHelp', UNDEFINED)
        url_for = context.get('url_for', UNDEFINED)
        locations = context.get('locations', UNDEFINED)
        _session = context.get('_session', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!-- CONTEXT HELP DIVS -->\n<div id="tooltipPool" style="display: none">\n  <!-- Where is key? -->\n  <div id="defaultLocationCH" class="tip">\n    ')
        __M_writer(str(encode_if_unicode( _("First location/location by default offered to users"))))
        __M_writer('\n  </div>\n  ')
        runtime._include_file(context, 'CHBookingRepetition.tpl', _template_uri)
        __M_writer('\n</div>\n<!-- END OF CONTEXT HELP DIVS -->\n\n\n<table align="center" width="95%">\n\n<!-- ==================== Manage Locations  ==================== -->\n<!-- =========================================================== -->\n<tr>\n  <td>\n    <table>\n    <tr>\n      <td class="titleUpCellTD" style="width: 160px;">\n        <span class="titleCellFormat">')
        __M_writer(str(encode_if_unicode( _('Available locations'))))
        __M_writer('</span>\n      </td>\n      <td bgcolor="white" valign="top" class="blacktext" style="padding-left: 12px;">\n')
        if locations:
            __M_writer('        <form action="')
            __M_writer(str(encode_if_unicode( url_for('rooms_admin.roomBooking-deleteLocation') )))
            __M_writer('" method="POST">\n          <input type="hidden" name="csrf_token" value="')
            __M_writer(str(encode_if_unicode( _session.csrf_token )))
            __M_writer('">\n          <p>\n')
            for loc in locations:
                __M_writer('              <input type="radio" name="location_id" value="')
                __M_writer(str(encode_if_unicode( loc.id )))
                __M_writer('">\n              <a href="')
                __M_writer(str(encode_if_unicode( url_for('rooms_admin.roomBooking-adminLocation', loc) )))
                __M_writer('">\n                ')
                __M_writer(str(encode_if_unicode( loc.name )))
                __M_writer('\n              </a><br>\n')
            __M_writer('            <input type="submit" class="i-button" value="')
            __M_writer(str(encode_if_unicode( _('Remove') )))
            __M_writer('" />\n          </p>\n        </form>\n')
        __M_writer('        <form action="')
        __M_writer(str(encode_if_unicode( url_for('rooms_admin.roomBooking-saveLocation') )))
        __M_writer('" method="POST">\n          <input type="hidden" name="csrf_token" value="')
        __M_writer(str(encode_if_unicode( _session.csrf_token )))
        __M_writer('">\n          <p>\n            <input type="text" id="newLocationName" name="newLocationName" value="" size="28" />\n            <input type="submit" class="i-button" value="')
        __M_writer(str(encode_if_unicode( _('Add') )))
        __M_writer('" />\n          </p>\n        </form>\n      </td>\n    </tr>\n')
        if locations:
            __M_writer('    <tr>\n      <td class="titleUpCellTD" style="width: 160px;">\n        <span class="titleCellFormat">')
            __M_writer(str(encode_if_unicode( _("Default location") )))
            __M_writer('</span>\n      </td>\n      <td bgcolor="white" valign="top" class="blacktext" style="padding-left: 12px;">\n        <form action="')
            __M_writer(str(encode_if_unicode( url_for('rooms_admin.roomBooking-setDefaultLocation') )))
            __M_writer('" method="POST">\n          <input type="hidden" name="csrf_token" value="')
            __M_writer(str(encode_if_unicode( _session.csrf_token )))
            __M_writer('">\n          <select name="location_id" id="defaultLocation">\n')
            for loc in locations:
                __M_writer('              <option value="')
                __M_writer(str(encode_if_unicode( loc.id )))
                __M_writer('" ')
                __M_writer(str(encode_if_unicode(' selected' if loc.is_default else '')))
                __M_writer(' >')
                __M_writer(str(encode_if_unicode( loc.name )))
                __M_writer('</option>\n')
            __M_writer('          </select>\n          <input type="submit" class="i-button" value="')
            __M_writer(str(encode_if_unicode( _('Change') )))
            __M_writer('">\n          ')
            __M_writer(str(encode_if_unicode( contextHelp('defaultLocationCH') )))
            __M_writer('\n        </form>\n      </td>\n    </tr>\n')
        __M_writer('    </table>\n    <br />\n  </td>\n</tr>\n</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"20": 0, "29": 1, "30": 5, "31": 5, "32": 7, "33": 7, "34": 21, "35": 21, "36": 24, "37": 25, "38": 25, "39": 25, "40": 26, "41": 26, "42": 28, "43": 29, "44": 29, "45": 29, "46": 30, "47": 30, "48": 31, "49": 31, "50": 34, "51": 34, "52": 34, "53": 38, "54": 38, "55": 38, "56": 39, "57": 39, "58": 42, "59": 42, "60": 47, "61": 48, "62": 50, "63": 50, "64": 53, "65": 53, "66": 54, "67": 54, "68": 56, "69": 57, "70": 57, "71": 57, "72": 57, "73": 57, "74": 57, "75": 57, "76": 59, "77": 60, "78": 60, "79": 61, "80": 61, "81": 66, "87": 81}, "uri": "RoomBookingAdmin.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingAdmin.tpl"}
__M_END_METADATA
"""
