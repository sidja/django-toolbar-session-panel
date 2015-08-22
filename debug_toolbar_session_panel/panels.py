# -*- coding: utf-8 -*-
from debug_toolbar.panels import DebugPanel 
from django.utils.translation import ugettext_lazy as _
from django.utils.datastructures import SortedDict
import json
import types

class SessionDebugPanel(DebugPanel):
    """
    Panel that displays session content
    """
    name = 'Session'
    template = 'debug_toolbar_session_panel/panel.html'
    has_content = True

    def nav_title(self):
        return _('Session')

    def title(self):
        return self.nav_title()

    def url(self):
        return ''

    def process_response(self, request, response):
        data = {'session':{
            'info': SortedDict([
                ('session_key',request.session.session_key),
                ('user', request.user),
                ('modified', request.session.modified),
                ('accessed', request.session.accessed)
                ]),
            'data' : SortedDict([(i[0], json.dumps(i[1], default=lambda o: o.__dict__)) if isinstance(i[1], types.InstanceType) else (i[0], i[1]) for i in request.session.items()] )
        }}
        self.record_stats(data)
