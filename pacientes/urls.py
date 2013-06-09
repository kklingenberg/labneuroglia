from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('pacientes.views',
    url(r'^$', 'index'),
    url(r'^exportar/paciente/csv$', 'export_pacientes_csv'),
    url(r'^exportar/paciente/pdf$', 'export_pacientes_pdf'),
    url(r'^exportar/evaluacionmotora/csv$', 'export_evalmotoras_csv'),
    url(r'^exportar/evaluacionmotora/pdf$', 'export_evalmotoras_pdf'),
    url(r'^exportar/evaluacionfuncional/csv$', 'export_evalfunc_csv'),
    url(r'^exportar/evaluacionfuncional/pdf$', 'export_evalfunc_pdf'),
    url(r'^exportar/examensignosvitales/csv$', 'export_esignosvitales_csv'),
    url(r'^exportar/examenfisico/csv$', 'export_efisico_csv'),
    url(r'^exportar/examenneurologico/csv$', 'export_eneurologico_csv'),
)
