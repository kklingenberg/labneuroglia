from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'labs.views.home', name='home'),
    # url(r'^labs/', include('labs.foo.urls')),
    url(r'^$', 'labs.views.home'),
    url(r'^respaldo$', 'labs.views.backup'),
    url(r'^viales/', include('viales.urls')),
    url(r'^vivero/', include('vivero.urls')),
    url(r'^pacientes/', include('pacientes.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
