# Session Debug Panel

This panel allow you to query your session after request.

## Install

With pip:

    pip install -e git+git://github.com/sidja/django-toolbar-session-panel.git#egg=debug_toolbar_session_panel

and in settings.py:

    INSTALLED_APPS += (
        'debug_toolbar_session_panel',
    )
    
    DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar_session_panel.panels.SessionDebugPanel',
]
than you will see something like:

<img src="https://dl.dropboxusercontent.com/u/4318926/Github/Screenshots/Django_debug_toolbar/Session_screen.PNG" />
