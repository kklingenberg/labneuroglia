from pacientes.models import Paciente, Familiar, EvaluacionMotora, EvaluacionFuncional, Neuroimagen, ExamenSignosVitales, ExamenFisico, ExamenNeurologico
from django.contrib import admin
from django.http import HttpResponseRedirect

class FamiliarInline(admin.StackedInline):
    model = Familiar
    extra = 0

class NeuroimagenInline(admin.StackedInline):
    model = Neuroimagen
    extra = 0

class PacienteAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'Demogr\u00E1ficos', {'fields': ['sexo', 'nacimiento', 'raza', 'raza_otro']}),
        (u'Gen\u00E9ticos', {'fields': ['test_genetico', 'tripletes']}),
        (u'Consentimiento', {'fields': ['fecha_consentimiento']}),
        (u'Historial de HD', {'fields': ['fecha_diagnostico', 'fecha_sintomas', 'fecha_tratamiento', 'medicacion', 'medicacion_glosa']}),
        (u'Historial neurol\u00F3gico', {'fields': ['enfermedades_pasadas', 'enfermedades_pasadas_glosa']}),
        (u'Historial de cirug\u00EDa', {'fields': ['cirugias', 'cirugias_glosa']}),
    ]
    inlines = [FamiliarInline, NeuroimagenInline]
    radio_fields = {
        'sexo': admin.HORIZONTAL,
        'raza': admin.VERTICAL,
        'test_genetico': admin.HORIZONTAL,
        'medicacion': admin.HORIZONTAL,
        'enfermedades_pasadas': admin.HORIZONTAL,
        'cirugias': admin.HORIZONTAL,
    }
    list_display = ('__unicode__', 'nacimiento', 'sexo', 'numero_familiares', 'evaluaciones_motoras', 'evaluaciones_funcionales', 'fecha_ultima_revision')
    list_filter = ['nacimiento', 'sexo']
    search_fields = ['id']
    date_hierarchy = 'nacimiento'
    save_as = True
    save_on_top = True
    actions = ['export_csv', 'export_pdf']

    def export_csv(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/pacientes/exportar/paciente/csv?ids={0}".format(",".join(ids)))
    export_csv.short_description = "Exportar seleccionados en formato CSV"

    def export_pdf(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/pacientes/exportar/paciente/pdf?ids={0}".format(",".join(ids)))
    export_pdf.short_description = "Exportar seleccionados en formato PDF"

admin.site.register(Paciente, PacienteAdmin)
#admin.site.register(Familiar)

class EvaluacionMotoraAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'fecha', 'efectuadas', 'total_puntaje')
    list_filter = ['fecha']
    search_fields = ['paciente__id']
    date_hierarchy = 'fecha'
    save_on_top = True
    actions = ['export_csv', 'export_pdf']

    def export_csv(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/pacientes/exportar/evaluacionmotora/csv?ids={0}".format(",".join(ids)))
    export_csv.short_description = "Exportar seleccionados en formato CSV"

    def export_pdf(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/pacientes/exportar/evaluacionmotora/pdf?ids={0}".format(",".join(ids)))
    export_pdf.short_description = "Exportar seleccionados en formato PDF"

admin.site.register(EvaluacionMotora, EvaluacionMotoraAdmin)

class EvaluacionFuncionalAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'Referecias', {'fields': ['paciente', 'fecha']}),
        (u'Cuestionario', {'fields': ['q{0}'.format(i) for i in range(1, 26)]}),
        (u'Evaluaci\u00F3n', {'fields': ['occupation', 'finances', 'chores', 'adl', 'care']}),
    ]
    radio_fields = dict(map(lambda q: (q, admin.HORIZONTAL), ['q{0}'.format(i) for i in range(1,26)]))
    list_display = ('__unicode__', 'fecha', 'preguntas_efectuadas', 'porcentaje_respuestas_afirmativas', 'total_capacidad_funcional')
    list_filter = ['fecha']
    search_fields = ['paciente__id']
    date_hierarchy = 'fecha'
    save_on_top = True
    actions = ['export_csv', 'export_pdf']

    def export_csv(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/pacientes/exportar/evaluacionfuncional/csv?ids={0}".format(",".join(ids)))
    export_csv.short_description = "Exportar seleccionados en formato CSV"

    def export_pdf(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/pacientes/exportar/evaluacionfuncional/pdf?ids={0}".format(",".join(ids)))
    export_pdf.short_description = "Exportar seleccionados en formato PDF"

admin.site.register(EvaluacionFuncional, EvaluacionFuncionalAdmin)
#admin.site.register(Neuroimagen)

class ExamenSignosVitalesAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha'
    list_filter = ['fecha']
    search_fields = ['paciente__id']
    list_display = ('__unicode__', 'fecha')
    actions = ['export_csv']

    def export_csv(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/pacientes/exportar/examensignosvitales/csv?ids={0}".format(",".join(ids)))
    export_csv.short_description = "Exportar seleccionados en formato CSV"

admin.site.register(ExamenSignosVitales, ExamenSignosVitalesAdmin)

class ExamenFisicoAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha'
    list_filter = ['fecha']
    search_fields = ['paciente__id']
    list_display = ('__unicode__', 'fecha')
    radio_fields = {
        'apariencia'   : admin.HORIZONTAL,
        'piel'         : admin.HORIZONTAL,
        'cabeza'       : admin.HORIZONTAL,
        'ojos'         : admin.HORIZONTAL,
        'pecho'        : admin.HORIZONTAL,
        'corazon'      : admin.HORIZONTAL,
        'abdomen'      : admin.HORIZONTAL,
        'extremidades' : admin.HORIZONTAL
    }
    actions = ['export_csv']

    def export_csv(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/pacientes/exportar/examenfisico/csv?ids={0}".format(",".join(ids)))
    export_csv.short_description = "Exportar seleccionados en formato CSV"

admin.site.register(ExamenFisico, ExamenFisicoAdmin)

class ExamenNeurologicoAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha'
    list_filter = ['fecha']
    search_fields = ['paciente__id']
    list_display = ('__unicode__', 'fecha')
    radio_fields = {
        'estado_mental'     : admin.HORIZONTAL,
        'nervios_craneales' : admin.HORIZONTAL,
        'sistema_motor'     : admin.HORIZONTAL,
        'sistema_sensorial' : admin.HORIZONTAL,
        'reflejos'          : admin.HORIZONTAL,
        'coordinacion'      : admin.HORIZONTAL
    }
    actions = ['export_csv']

    def export_csv(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/pacientes/exportar/examenneurologico/csv?ids={0}".format(",".join(ids)))
    export_csv.short_description = "Exportar seleccionados en formato CSV"

admin.site.register(ExamenNeurologico, ExamenNeurologicoAdmin)

