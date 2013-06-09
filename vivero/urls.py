from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('vivero.views',
    url(r'^$', 'index'),
    url(r'^ratones/(?P<raton_id>\d+)/$', 'detail'),
    url(r'^ratones/(?P<raton_id>\d+)/reserva/$', 'reservationform'),
    url(r'^ratones/(?P<raton_id>\d+)/reservar/$', 'reserve'),
    url(r'^revisiones/(?P<revision_id>\d+)/$', 'revision'),
    url(r'^reservas$', 'reservations'),
    url(r'^bitacora$', 'log'),
    url(r'^histograma$', 'histogram'),
    # Exportacion de datos
    url(r'^exportar/raton/csv$', 'export_ratones_csv'),
    url(r'^exportar/raton/pdf$', 'export_ratones_pdf'),
    url(r'^exportar/reserva/csv$', 'export_reservas_csv'),
    url(r'^exportar/reserva/pdf$', 'export_reservas_pdf'),
    url(r'^exportar/revision/csv$', 'export_revisiones_csv'),
    url(r'^exportar/revision/pdf$', 'export_revisiones_pdf'),
)

