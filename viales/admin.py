from viales.models import Stock, Linea, Vial
from laboratorio.base_admin import BaseAdmin
from django.contrib import admin
import datetime
from django.http import HttpResponseRedirect

admin.site.register(Stock)
admin.site.register(Linea)

class VialAdmin(BaseAdmin):
    exclude = ('vigente', 'usuario', 'usuario_descongela',)
    fieldsets = [
        (u'', {'fields': ['linea', 'stock', 'ubicacion', 'fecha', 'observaciones']}),
        (u'Descongelaci\u00F3n', {'fields': ['descongelacion'], 'classes': ['collapse']})
    ]
    list_display = ('__unicode__', 'stock', 'fecha', 'vigente', 'usuario', 'descongelado_por')
    list_filter = ['stock', 'linea', 'vigente', 'fecha']
    date_hierarchy = 'fecha'
    save_as = True
    save_on_top = True
    actions = ['descongelar', 'export_csv', 'export_pdf']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        obj.save()

    def descongelar(self, request, queryset):
        hoy = datetime.date.today()
        validos = queryset.filter(vigente__iexact='S').update(descongelacion=hoy, usuario_descongela=request.user, vigente='N')
        self.message_user(request, u"{0} viales descongelados de los {1} seleccionados".format(validos, queryset.count()))
    descongelar.short_description = "Descongelar viales"

    def export_csv(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/viales/exportar/vial/csv?ids={0}".format(",".join(ids)))
    export_csv.short_description = "Exportar seleccionados en formato CSV"

    def export_pdf(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/viales/exportar/vial/pdf?ids={0}".format(",".join(ids)))
    export_pdf.short_description = "Exportar seleccionados en formato PDF"

admin.site.register(Vial, VialAdmin)
