# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528621933.560674
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingBlockingList.tpl'
_template_uri = 'RoomBookingBlockingList.tpl'
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
        url_for = context.get('url_for', UNDEFINED)
        blockings = context.get('blockings', UNDEFINED)
        len = context.get('len', UNDEFINED)
        str = context.get('str', UNDEFINED)
        formatDate = context.get('formatDate', UNDEFINED)
        rh = context.get('rh', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<h2 class="page-title">\n    ')
        __M_writer(str(encode_if_unicode("My Blockings" if rh.only_mine else "Blockings")))
        __M_writer('\n</h2>\n<br />\n')
        if blockings:
            __M_writer('    <br />\n    <table class="blockingTable">\n        <thead>\n        <tr>\n          <td class="dataCaptionFormat">')
            __M_writer(str(encode_if_unicode( _("Period"))))
            __M_writer('</td>\n          <td class="dataCaptionFormat">')
            __M_writer(str(encode_if_unicode( _("Owner"))))
            __M_writer('</td>\n          <td class="dataCaptionFormat">')
            __M_writer(str(encode_if_unicode( _("Rooms"))))
            __M_writer('</td>\n          <td class="dataCaptionFormat">')
            __M_writer(str(encode_if_unicode( _("Reason"))))
            __M_writer('</td>\n          <td class="dataCaptionFormat">')
            __M_writer(str(encode_if_unicode( _("Actions"))))
            __M_writer('</td>\n        </tr>\n        </thead>\n        ')
            lastBlock = None 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['lastBlock'] if __M_key in __M_locals_builtin_stored]))
            __M_writer('\n')
            for block in blockings:
                if lastBlock:
                    __M_writer('                <tbody class="blockingSpacer"><tr><td></td></tr></tbody>\n')
                __M_writer('            <tbody>\n            <tr class="blockingHover blockingPadding">\n                <td>')
                __M_writer(str(encode_if_unicode( formatDate(block.start_date) )))
                __M_writer('&nbsp;&mdash;&nbsp;')
                __M_writer(str(encode_if_unicode( formatDate(block.end_date) )))
                __M_writer('</td>\n                <td>')
                __M_writer(str(encode_if_unicode( block.created_by_user.full_name )))
                __M_writer('</td>\n                <td>')
                __M_writer(str(encode_if_unicode( len(block.blocked_rooms) )))
                __M_writer(' room')
                __M_writer(str(encode_if_unicode( (len(block.blocked_rooms) != 1 and 's' or '') )))
                __M_writer('</td>\n                <td>')
                __M_writer(str(encode_if_unicode( block.reason )))
                __M_writer('</td>\n                <td><a href="')
                __M_writer(str(encode_if_unicode( url_for('rooms.blocking_details', blocking_id=str(block.id)) )))
                __M_writer('">Details</a> | <a href="#" class="blockingShowRooms">Show rooms</a></td>\n            </tr>\n            <tr class="blockingHover blockingRoomList">\n                <td colspan="2"></td>\n                <td colspan="2">\n                    <div>\n                        ')
                __M_writer(str(encode_if_unicode( '<br />'.join('<a href="{}">{}</a>'.format(url_for('rooms.roomBooking-roomDetails', br.room), br.room.full_name) for br in block.blocked_rooms) )))
                __M_writer('\n                    </div>\n                </td>\n                <td></td>\n            </tr>\n            </tbody>\n            ')
                lastBlock = block 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['lastBlock'] if __M_key in __M_locals_builtin_stored]))
                __M_writer('\n')
            __M_writer('    </table>\n\n    <script type="text/javascript">\n        $(\'.blockingShowRooms\').on(\'click\', function(e) {\n            e.preventDefault();\n            var $this = $(this);\n            var roomList = $this.closest(\'tr\').next(\'.blockingRoomList\');\n            var show = roomList.is(\':hidden\');\n            $this.text(show ? $T(\'Hide rooms\') : $T(\'Show rooms\'));\n            roomList.toggle(show);\n            $this.closest(\'tbody\').toggleClass(\'hasRoomList\', show);\n        });\n    </script>\n')
        else:
            __M_writer('    <br />\n    <em>None found.</em>\n    <br />\n')
        __M_writer('<br />\nFilter blockings by creator:\n<a href="')
        __M_writer(str(encode_if_unicode( url_for('rooms.blocking_list', timeframe=rh.timeframe, only_mine=False) )))
        __M_writer('" class="')
        __M_writer(str(encode_if_unicode( ('' if rh.only_mine else 'active') )))
        __M_writer('">all users</a> |\n<a href="')
        __M_writer(str(encode_if_unicode( url_for('rooms.blocking_list', timeframe=rh.timeframe, only_mine=True) )))
        __M_writer('" class="')
        __M_writer(str(encode_if_unicode( ('active' if rh.only_mine else '') )))
        __M_writer('">only myself</a>\n<br />\nFilter blockings by date:\n<a href="')
        __M_writer(str(encode_if_unicode( url_for('rooms.blocking_list', only_mine=rh.only_mine, timeframe='recent') )))
        __M_writer('" class="')
        __M_writer(str(encode_if_unicode( ('active' if rh.timeframe == 'recent' else '') )))
        __M_writer('">active and future blockings</a> |\n<a href="')
        __M_writer(str(encode_if_unicode( url_for('rooms.blocking_list', only_mine=rh.only_mine, timeframe='year') )))
        __M_writer('" class="')
        __M_writer(str(encode_if_unicode( ('active' if rh.timeframe == 'year' else '') )))
        __M_writer('">all blockings for this year</a> |\n<a href="')
        __M_writer(str(encode_if_unicode( url_for('rooms.blocking_list', only_mine=rh.only_mine, timeframe='all') )))
        __M_writer('" class="')
        __M_writer(str(encode_if_unicode( ('active' if rh.timeframe == 'all' else '') )))
        __M_writer('">all blockings</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"20": 0, "31": 1, "32": 2, "33": 2, "34": 5, "35": 6, "36": 10, "37": 10, "38": 11, "39": 11, "40": 12, "41": 12, "42": 13, "43": 13, "44": 14, "45": 14, "46": 17, "50": 17, "51": 18, "52": 19, "53": 20, "54": 22, "55": 24, "56": 24, "57": 24, "58": 24, "59": 25, "60": 25, "61": 26, "62": 26, "63": 26, "64": 26, "65": 27, "66": 27, "67": 28, "68": 28, "69": 34, "70": 34, "71": 40, "75": 40, "76": 42, "77": 55, "78": 56, "79": 60, "80": 62, "81": 62, "82": 62, "83": 62, "84": 63, "85": 63, "86": 63, "87": 63, "88": 66, "89": 66, "90": 66, "91": 66, "92": 67, "93": 67, "94": 67, "95": 67, "96": 68, "97": 68, "98": 68, "99": 68, "105": 99}, "uri": "RoomBookingBlockingList.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingBlockingList.tpl"}
__M_END_METADATA
"""
