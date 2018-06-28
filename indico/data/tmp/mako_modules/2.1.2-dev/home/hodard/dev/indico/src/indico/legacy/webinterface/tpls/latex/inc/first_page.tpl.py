# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1528744688.020788
_enable_loop = True
_template_filename = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/inc/first_page.tpl'
_template_uri = '/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/inc/first_page.tpl'
_source_encoding = 'utf-8'
from indico.util.json import dumps as j
from indico.util.string import encode_if_unicode, sanitize_html
from indico.util.string import render_markdown_utf8 as m
from indico.util.i18n import _
_exports = []


def render_body(context,event,title,show_dates=False,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,show_dates=show_dates,event=event,title=title)
        url = context.get('url', UNDEFINED)
        latex_escape = context.get('latex_escape', UNDEFINED)
        tz = context.get('tz', UNDEFINED)
        logo_img = context.get('logo_img', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n\\begin{titlepage}\n\n\\thispagestyle{fancy}\n\n\\begin{center}\n    \\fontsize{30}{36}\\selectfont \\textbf{')
        __M_writer(latex_escape(str(encode_if_unicode(event.title.encode('utf-8') ))))
        __M_writer('}\n\\end{center}\n\n\\vspace{2em}\n\n')
        if show_dates:
            __M_writer('    \\begin{center}\n        \\Large\n        ')
            __M_writer(latex_escape(str(encode_if_unicode(event.start_dt.astimezone(tz).strftime("%A %d %B %Y") ))))
            __M_writer(' -\n        ')
            __M_writer(latex_escape(str(encode_if_unicode(event.end_dt.astimezone(tz).strftime("%A %d %B %Y") ))))
            __M_writer('\n    \\end{center}\n\n')
            if event.venue_name:
                __M_writer('        \\begin{center}\n            \\Large\n            ')
                __M_writer(latex_escape(str(encode_if_unicode(event.venue_name ))))
                __M_writer('\n        \\end{center}\n')
            __M_writer('\n    \\vspace{2em}\n')
        __M_writer('\n')
        if logo_img:
            __M_writer('    \\begin{figure}[h!]\n        \\includegraphics[max width=0.85\\linewidth, min width=0.5\\linewidth]{')
            __M_writer(str(encode_if_unicode(logo_img)))
            __M_writer('}\n        \\centering\n    \\end{figure}\n\n    \\vspace{4em}\n')
        else:
            __M_writer('    \\vspace{2em}\n')
        __M_writer('\n\n\n\\vspace{2em}\n\n\\begin{center}\n    {\\fontsize{35}{42}\\selectfont \\sffamily \\textbf{')
        __M_writer(latex_escape(str(encode_if_unicode(title ))))
        __M_writer('}}\n\\end{center}\n\n')
        if url:
            __M_writer('    \\fancyfoot[C]{\\tt ')
            __M_writer(latex_escape(str(encode_if_unicode(url ))))
            __M_writer('}\n')
        else:
            __M_writer('    \\fancyfoot[C]{}\n')
        __M_writer('\n\\end{titlepage}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"20": 1, "29": 1, "30": 8, "31": 8, "32": 13, "33": 14, "34": 16, "35": 16, "36": 17, "37": 17, "38": 20, "39": 21, "40": 23, "41": 23, "42": 26, "43": 29, "44": 30, "45": 31, "46": 32, "47": 32, "48": 37, "49": 38, "50": 40, "51": 46, "52": 46, "53": 49, "54": 50, "55": 50, "56": 50, "57": 51, "58": 52, "59": 54, "65": 59}, "uri": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/inc/first_page.tpl", "filename": "/home/hodard/dev/indico/src/indico/legacy/webinterface/tpls/latex/inc/first_page.tpl"}
__M_END_METADATA
"""
