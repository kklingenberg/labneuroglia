from vivero.models import Linea, Genotipo, Raton, Reserva, Revision, ImagenRaton, VideoRaton, Historico
from django.contrib import admin
from django.db.models import Q, Count
from django.http import HttpResponseRedirect
import datetime
import re

admin.site.register(Linea)
admin.site.register(Genotipo)

class ImagenInline(admin.StackedInline):
    model = ImagenRaton
    extra = 0

class VideoInline(admin.StackedInline):
    model = VideoRaton
    extra = 0

def save_history(mice, state, user, event):
    for mouse in mice:
        h = Historico()
        h.raton = mouse
        h.estado = state
        h.evento = event
        h.usuario = user
        h.save()


class RatonAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'Identificaci\u00F3n',  {'fields': ['linea', 'camada', 'numero']}),
        (u'Caracter\u00EDsticas', {'fields': ['sexo', 'genotipo', 'regenotipo', 'nacimiento', 'colonia', 'estado', 'observaciones']}),
        (u'Padres', {'fields': ['padre', 'madre'], 'classes': ['collapse']}),
        (u'Muerte', {'fields': ['muerte'], 'classes': ['collapse']}),
    ]
    list_display = ('__unicode__', 'sexo', 'genotipo', 'estado', 'nacimiento', 'edad', 'reservado_verbose')
    list_filter = ['sexo', 'estado', 'nacimiento', 'linea', 'genotipo']
    inlines = [ImagenInline, VideoInline]
    search_fields = ['numero']
    date_hierarchy = 'nacimiento'
    radio_fields = {"estado": admin.VERTICAL, "sexo": admin.HORIZONTAL}
    save_as = True
    save_on_top = True
    actions = [
        'register_deaths',
        'register_sacrifices',
        'register_euthanasia',
        'reserve',
        'export_csv',
        'export_pdf'
    ]

    def register_deaths(self, request, queryset):
        subset = queryset.filter(Q(estado__iexact='V') | Q(estado__iexact='A'))
        save_history(subset, 'M', request.user, "muerte")
        deaths = subset.update(estado='M', muerte=datetime.date.today())
        self.message_user(request, u"{0} ratones registrados muertos de los {1} seleccionados".format(deaths, queryset.count()))
    register_deaths.short_description = "Registrar muertes"

    def register_sacrifices(self, request, queryset):
        subset = queryset.filter(Q(estado__iexact='V') | Q(estado__iexact='A'))
        save_history(subset, 'S', request.user, "sacrificado")
        sacrifices = subset.update(estado='S', muerte=datetime.date.today())
        self.message_user(request, u"{0} ratones registrados sacrificados de los {1} seleccionados".format(sacrifices, queryset.count()))
    register_sacrifices.short_description = "Registrar ratones sacrificados"

    def register_euthanasia(self, request, queryset):
        subset = queryset.filter(Q(estado__iexact='V') | Q(estado__iexact='A'))
        save_history(subset, 'E', request.user, "eutanasia")
        deaths = subset.update(estado='E', muerte=datetime.date.today())
        self.message_user(request, u"{0} ratones registrados muertos por eutanasia de los {1} seleccionados".format(deaths, queryset.count()))
    register_euthanasia.short_description = "Registrar eutanasias"

    def reserve(self, request, queryset):
        posibles = queryset.filter(estado__iexact='V')
        posibles = filter(lambda x: x.reservable(), posibles)
        if len(posibles) == 0:
            self.message_user(request, u"No es posible reservar ning\u00FAn rat\u00F3n seleccionado: su estado debe ser \"disponible\" y no puede estar reservado ya")
        elif len(posibles) > 1:
            self.message_user(request, u"S\u00F3lo es posible reservar un rat\u00F3n a la vez")
        else:
            return HttpResponseRedirect("/vivero/ratones/{0}/reserva/?prev={1}".format(posibles[0].id, request.get_full_path()))
    reserve.short_description = u"Reservar rat\u00F3n"

    def export_csv(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/vivero/exportar/raton/csv?ids={0}".format(",".join(ids)))
    export_csv.short_description = "Exportar seleccionados en formato CSV"

    def export_pdf(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/vivero/exportar/raton/pdf?ids={0}".format(",".join(ids)))
    export_pdf.short_description = "Exportar seleccionados en formato PDF"

    def save_model(self, request, obj, form, change):
        # Anotar fecha de muerte si falta
        if change:
            old = Raton.objects.get(pk=obj.pk)
            if (old.vive()) and (not obj.vive()) and (obj.muerte is None):
                obj.muerte = datetime.date.today()
        else:
            if (not obj.vive()) and (obj.muerte is None):
                obj.muerte = datetime.date.today()
        obj.save()
        # anotar en historico
        h = Historico()
        h.raton = obj
        h.estado = obj.estado
        h.evento = u"modificaci\u00F3n" if change else u"ingreso"
        h.usuario = request.user
        h.save()

admin.site.register(Raton, RatonAdmin)

class ReservaAdmin(admin.ModelAdmin):
    exclude = ('usuario',)
    list_display = ('raton', 'usuario', 'fecha', 'edad_reserva')
    list_filter = ['fecha']
    date_hierarchy = 'fecha'
    radio_fields = {"tipo": admin.HORIZONTAL}
    save_on_top = True
    actions = ['export_csv', 'export_pdf']

    def export_csv(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/vivero/exportar/reserva/csv?ids={0}".format(",".join(ids)))
    export_csv.short_description = "Exportar seleccionadas en formato CSV"

    def export_pdf(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/vivero/exportar/reserva/pdf?ids={0}".format(",".join(ids)))
    export_pdf.short_description = "Exportar seleccionados en formato PDF"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "raton":
            # Para distinguir si se esta editando o no
            editing_id = re.search("[0-9]+", request.path)
            if editing_id is not None:
                raton_pk = Reserva.objects.get(pk=editing_id.group(0)).raton.pk
                kwargs["queryset"] = Raton.objects.filter(pk=raton_pk)
            else:
                kwargs["queryset"] = Raton.objects.filter(estado__iexact='V').annotate(num_reservas=Count('reserva')).filter(num_reservas=0)
        return super(ReservaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def queryset(self, request):
        if request.user.is_superuser or request.user.groups.filter(name='superusuarios lab').count() > 0:
            return Reserva.objects.all()
        return Reserva.objects.filter(usuario=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        obj.save()

admin.site.register(Reserva, ReservaAdmin)

class RevisionAdmin(admin.ModelAdmin):
    list_display = ('raton', 'fecha', 'puntaje')
    list_filter = ['fecha']
    date_hierarchy = 'fecha'
    save_on_top = True
    actions = ['export_csv', 'export_pdf']

    def export_csv(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/vivero/exportar/revision/csv?ids={0}".format(",".join(ids)))
    export_csv.short_description = "Exportar seleccionadas en formato CSV"

    def export_pdf(self, request, queryset):
        ids = map(lambda x: str(x.pk), queryset)
        return HttpResponseRedirect("/vivero/exportar/revision/pdf?ids={0}".format(",".join(ids)))
    export_pdf.short_description = "Exportar seleccionados en formato PDF"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "raton":
            kwargs["queryset"] = Raton.objects.filter(Q(estado__iexact='V') | Q(estado__iexact='A'))
        return super(RevisionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.save()
        # anotar en historico
        h = Historico()
        h.raton = obj.raton
        h.estado = obj.raton.estado
        h.usuario = request.user
        h.evento = u"revisi\u00F3n"
        h.save()

admin.site.register(Revision, RevisionAdmin)

