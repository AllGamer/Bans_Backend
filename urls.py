from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^Bans_Backend/', include('Bans_Backend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^bansapi/$', 'api.views.index'),
    #(r'^bansapi/heartbeat.php\?apikey=(?P<api_key>)$,players=(?P<online>)$', 'api.views.heartbeat'),
    (r'^bansapi/heartbeat/(?P<api_key>\d+)$', 'api.views.heartbeat'),
    (r'^bansapi/ban.php$', 'api.views.ban'),
    (r'^bansapi/unban.php$', 'api.views.unban'),
)
