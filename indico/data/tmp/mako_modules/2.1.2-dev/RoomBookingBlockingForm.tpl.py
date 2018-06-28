# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528621903.394105
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingBlockingForm.tpl'
_template_uri = 'RoomBookingBlockingForm.tpl'
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
        inlineContextHelp = context.get('inlineContextHelp', UNDEFINED)
        blocking = context.get('blocking', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()

        start_date = blocking.start_date if blocking else form.start_date.data
        end_date = blocking.end_date if blocking else form.end_date.data
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['start_date','end_date'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<div style="width:80%;">\n    <h2 class="page-title">\n')
        if not blocking:
            __M_writer('             ')
            __M_writer(str(encode_if_unicode( _("New Blocking"))))
            __M_writer('\n')
        else:
            __M_writer('             ')
            __M_writer(str(encode_if_unicode( _("Modify Blocking"))))
            __M_writer('\n')
        __M_writer('    </h2>\n')
        if not blocking:
            __M_writer('        <em>')
            __M_writer(str(encode_if_unicode( _("""When blocking rooms nobody but you, the rooms' managers and those users/groups you specify in the "Allowed users" list will be able to create bookings for the specified rooms in the given timeframe.
        You can also block rooms you do not own - however, those blockings have to be approved by the owners of those rooms.""") )))
            __M_writer('</em>\n        <br />\n')
        __M_writer('</div>\n\n<form id="blockingForm" method="post">\n    ')
        __M_writer(str(encode_if_unicode( form.csrf_token() )))
        __M_writer('\n    ')
        __M_writer(str(encode_if_unicode( form.blocked_rooms() )))
        __M_writer('\n    <table cellpadding="0" cellspacing="0" border="0" width="80%">\n        <tr>\n            <td class="intermediateleftvtab" style="border-left: 2px solid #777777; border-right: 2px solid #777777; font-size: xx-small;" width="100%">&nbsp;</td> <!-- lastvtabtitle -->\n        </tr>\n        <tr>\n            <td class="bottomvtab" width="100%">\n                <table width="100%" cellpadding="0" cellspacing="0" class="htab" border="0">\n                    <tr>\n                        <td class="maincell">\n')
        if errors:
            __M_writer('                                <p class="error-message">')
            __M_writer(str(encode_if_unicode( _("Saving failed.") )))
            __M_writer('<br>')
            __M_writer(str(encode_if_unicode( '<br>'.join(errors) )))
            __M_writer('</p>\n')
        __M_writer('                            <table width="100%" align="left" border="0">\n                                <!-- WHEN -->\n                                <tr>\n                                    <td class="titleUpCellTD" valign="top"><span class="titleCellFormat">')
        __M_writer(str(encode_if_unicode( _("Period") )))
        __M_writer('</span></td>\n                                    <td bgcolor="white" width="100%">\n                                        <div id="dateRange"></div>\n                                    </td>\n                                </tr>\n                                <tr><td>&nbsp;</td></tr>\n                                <!-- REASON -->\n                                <tr>\n                                    <td class="titleUpCellTD" valign="top"><span class="titleCellFormat"> ')
        __M_writer(str(encode_if_unicode( _("Reason"))))
        __M_writer(' ')
        __M_writer(str(encode_if_unicode(inlineContextHelp(_("<b>Required.</b> The justification for blocking. Will be displayed to users trying to book.")))))
        __M_writer('</span></td>\n                                    <td bgcolor="white" width="100%">\n                                        ')
        __M_writer(str(encode_if_unicode( form.reason(rows=3, cols=50) )))
        __M_writer('\n                                    </td>\n                                </tr>\n                                <tr><td>&nbsp;</td></tr>\n                                <!-- ROOMS -->\n                                <tr>\n                                    <td class="titleUpCellTD" valign="top"><span class="titleCellFormat"> ')
        __M_writer(str(encode_if_unicode( _("Rooms"))))
        __M_writer(' ')
        __M_writer(str(encode_if_unicode(inlineContextHelp(_("These rooms will be blocked. Note that the room owner will have to confirm the blocking first unless it is owned by you.")))))
        __M_writer('</span></td>\n                                    <td bgcolor="white" width="100%">\n                                        <div id="roomList" class="PeopleListDiv"></div>\n                                        <div id="roomChooser"></div>\n                                        <div id="roomAddButton"></div>\n                                    </td>\n                                </tr>\n                                <tr><td>&nbsp;</td></tr>\n                                <!-- ACL -->\n                                <tr>\n                                    <td class="titleUpCellTD" valign="top"><span class="titleCellFormat"> ')
        __M_writer(str(encode_if_unicode( _("Allowed users/groups"))))
        __M_writer(' ')
        __M_writer(str(encode_if_unicode(inlineContextHelp(_("These users/groups are allowed to book the selected rooms during the blocking. Note that you as the creator of the blocking are always allowed to book them.")))))
        __M_writer('</span></td>\n                                    <td bgcolor="white" width="100%">\n                                        ')
        __M_writer(str(encode_if_unicode( form.principals() )))
        __M_writer('\n                                    </td>\n                                </tr>\n                                <tr><td>&nbsp;</td></tr>\n                                <!-- ACTIONS -->\n                                <tr>\n                                   <td colspan="2">\n                                       <table style="width: 100%; background-color: rgb(236, 236, 236); border-top: 1px dashed rgb(119, 119, 119);">\n                                           <tr>\n                                               <td class="titleUpCellTD"></td>\n                                               <td>\n                                                   <input id="submitBlocking" type="submit" class="btn" value="')
        __M_writer(str(encode_if_unicode(_('Create the blocking') if not blocking else _('Save'))))
        __M_writer('" disabled>\n                                               </td>\n                                           </tr>\n                                       </table>\n                                   </td>\n                                </tr>\n                            </table>\n                        </td>\n                    </tr>\n                </table>\n            </td>\n        </tr>\n    </table>\n</form>\n\n<script>\n    $(document).ready(function() {\n        $(\'#dateRange\').daterange({\n')
        if blocking:
            __M_writer("            labels: ['', ''],\n")
        __M_writer("            fieldNames: ['start_date', 'end_date'],\n            allowPast: ")
        __M_writer(str(encode_if_unicode( 'false' if not blocking else 'true' )))
        __M_writer(',\n            disabled: ')
        __M_writer(str(encode_if_unicode( 'false' if not blocking else 'true' )))
        __M_writer(",\n            startDate: '")
        __M_writer(str(encode_if_unicode( start_date.day )))
        __M_writer('/')
        __M_writer(str(encode_if_unicode( start_date.month )))
        __M_writer('/')
        __M_writer(str(encode_if_unicode( start_date.year )))
        __M_writer("',\n            endDate: '")
        __M_writer(str(encode_if_unicode( end_date.day )))
        __M_writer('/')
        __M_writer(str(encode_if_unicode( end_date.month )))
        __M_writer('/')
        __M_writer(str(encode_if_unicode( end_date.year )))
        __M_writer('\'\n        });\n\n        var pm = new IndicoUtil.parameterManager();\n        var hasRooms = false;\n\n        $(\'#submitBlocking\').on(\'click\', function(){\n            if (!pm.check()) {\n                return false;\n            }\n            else if(!hasRooms) {\n                new AlertPopup($T("Warning"), $T("Please add at least one room.")).open();\n                return false;\n            }\n')
        if not blocking:
            __M_writer('                new ConfirmPopup($T("Create blocking"), $T("Do you want to create the blocking? Please note that the start and end date cannot be changed after creation."), function(confirmed) {\n                    if(confirmed) {\n                        $("#blockingForm").submit();\n                    }\n                }).open();\n                return false;\n')
        else:
            __M_writer('                return true;\n')
        __M_writer('        });\n\n        var serializeRooms = function() {\n            var roomGuids = [];\n            enumerate(blockedRoomList.getAll(), function(value, key) {\n                roomGuids.push(key);\n            });\n            hasRooms = (roomGuids.length > 0);\n            $(\'#blocked_rooms\').val(Json.write(roomGuids));\n        };\n\n\n        var blockedRoomList = new RoomListWidget(\'user-list\', function(roomToRemove, setResult) {\n            setResult(true);\n            blockedRoomList.set(roomToRemove, null);\n            serializeRooms();\n        }, true);\n        var roomSelectedBefore = JSON.parse($(\'#blocked_rooms\').val());\n        $E(\'roomList\').set(blockedRoomList.draw());\n\n        var roomChooser = new SelectRemoteWidget(\'roomBooking.locationsAndRooms.listWithGuids\', {isActive: true}, function() {\n            $E(\'roomChooser\').set(roomChooser.draw(), addRoomButton);\n            // sort by room name. we cannot do it serverside since objects are not ordered\n            $(\'#roomChooser select > option\').detach().sort(function(a, b) {\n                return strnatcmp($(a).text().toLowerCase(), $(b).text().toLowerCase());\n            }).appendTo($(\'#roomChooser select\'));\n\n            // Preselect default if we have any\n            $.each(roomSelectedBefore, function(i, id) {\n                var roomName = $(\'option\', roomChooser.select.dom).filter(function() {\n                    return this.value == id;\n                }).text();\n                blockedRoomList.set(id, roomName);\n            });\n            serializeRooms(); // Shouldn\'t be necessary but let\'s stay on the safe side\n            $(\'#submitBlocking\').prop(\'disabled\', false);\n        }, null, null, null, false);\n        var addRoomButton = Html.input("button", {style:{marginRight: pixels(5)}}, $T(\'Add Room\') );\n        addRoomButton.observeClick(function(setResult){\n            var selectedValue = roomChooser.select.get();\n            var roomName = roomChooser.select.dom.options[roomChooser.select.dom.selectedIndex].innerHTML; // horrible..\n            blockedRoomList.set(selectedValue, roomName);\n            serializeRooms();\n        });\n        $E(\'roomAddButton\').set();\n\n        pm.add($E(\'reason\'), \'text\', false);\n    });\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"20": 0, "29": 1, "36": 4, "37": 8, "38": 9, "39": 9, "40": 9, "41": 10, "42": 11, "43": 11, "44": 11, "45": 13, "46": 14, "47": 15, "48": 15, "50": 16, "51": 19, "52": 22, "53": 22, "54": 23, "55": 23, "56": 33, "57": 34, "58": 34, "59": 34, "60": 34, "61": 34, "62": 36, "63": 39, "64": 39, "65": 47, "66": 47, "67": 47, "68": 47, "69": 49, "70": 49, "71": 55, "72": 55, "73": 55, "74": 55, "75": 65, "76": 65, "77": 65, "78": 65, "79": 67, "80": 67, "81": 78, "82": 78, "83": 96, "84": 97, "85": 99, "86": 100, "87": 100, "88": 101, "89": 101, "90": 102, "91": 102, "92": 102, "93": 102, "94": 102, "95": 102, "96": 103, "97": 103, "98": 103, "99": 103, "100": 103, "101": 103, "102": 117, "103": 118, "104": 124, "105": 125, "106": 127, "112": 106}, "uri": "RoomBookingBlockingForm.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/RoomBookingBlockingForm.tpl"}
__M_END_METADATA
"""
