from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^factoryState/', include('factoryState.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^command/', 'command.views.command'),
     url(r'^json/', 'command.views.json'),
     url(r'^interface/', 'interface.views.interface'),
     url(r'^$', 'interface.views.interface'),
     url(r'^startup/', 'command.views.startup'),
     url(r'^order/', 'order.views.order'),
     url(r'^pendingCommands/', 'command.views.pendingCommands'),
     url(r'^deleteCommand/', 'command.views.deleteCommand'),
     url(r'^tinyGParameter/', 'command.views.tinyGParameter'),
     url(r'^panelParameter/', 'panel.views.panelParameter'),
     url(r'^factoryState/', 'command.views.factoryState'),
     url(r'^action/', 'action.views.action'),
     url(r'^renderAction/$','command.views.renderAction'),
     url(r'^pendingPoints/$','point.views.pendingPoints'),
     url(r'^deletePoint/$','point.views.deletePoint'),
     url(r'^deleteAllPoints/$','point.views.deleteAllPoints'),
)
