from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^factoryState/', include('factoryState.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^command/', 'command.views.command'),
     url(r'^json/', 'command.views.json'),
     url(r'^interface/', 'command.views.interface'),
     url(r'^/', 'command.views.interface'),
     url(r'^testing/', 'command.views.testing'),
     url(r'^startup/', 'command.views.startup'),
     url(r'^order/', 'order.views.order'),
     url(r'^pendingCommands/', 'command.views.pendingCommands'),
     url(r'^deleteCommand/', 'command.views.deleteCommand'),
     url(r'^tinyGParameter/', 'command.views.tinyGParameter'),
     url(r'^panelParameter/', 'panel.views.panelParameter'),
     url(r'^factoryState/', 'command.views.factoryState'),

)
