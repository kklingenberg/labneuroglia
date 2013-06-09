from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('viales.views',
    url(r'^$', 'index'),
    url(r'^ultimomes$', 'lastmonth'),
    url(r'^bitacora$', 'log'),
    # Exportacion
    url(r'^exportar/vial/csv$', 'export_viales_csv'),
    url(r'^exportar/vial/pdf$', 'export_viales_pdf'),
)
