# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from laboratorio.exportable import CSVExportable, PDFExportable


class Linea(models.Model):
    "Líneas genéticas"

    linea = models.CharField(verbose_name=u'línea genética', max_length=100)

    class Meta:
        verbose_name = u'línea genética'
        verbose_name_plural = u'líneas genéticas'

    def __unicode__(self):
        return self.linea


class Genotipo(models.Model):
    "Lista de genotipos"

    genotipo = models.CharField(verbose_name='genotipo', max_length=100)

    def __unicode__(self):
        return self.genotipo


class Raton(models.Model, CSVExportable, PDFExportable):
    "Ratones de laboratorio"

    # Identificacion del animal
    linea = models.ForeignKey(Linea, verbose_name=u'línea genética')
    camada = models.CharField(max_length='100')
    numero = models.IntegerField(verbose_name=u'número')
    # Otras caracteristicas
    sexos = (
        (u'F', u'Femenino'),
        (u'M', u'Masculino'),)
    sexo = models.CharField(max_length=1, default='F', choices=sexos)
    genotipo = models.ForeignKey(
        Genotipo,
        related_name='raton_genotipo_set',
        blank=True,
        null=True)
    regenotipo = models.ForeignKey(
        Genotipo,
        related_name='raton_regenotipo_set',
        blank=True,
        null=True)
    nacimiento = models.DateField(verbose_name='fecha de nacimiento')
    colonia = models.CharField(max_length=100)
    estados = (
        (u'V', u'Disponible'),
        (u'A', u'Ocupado'),
        (u'S', u'Sacrificado'),
        (u'M', u'Muerto'),
        (u'E', u'Eutanasia'),)
    estado = models.CharField(max_length=1, default='V', choices=estados)
    muerte = models.DateField(
        verbose_name="fecha de muerte",
        blank=True,
        null=True)
    observaciones = models.TextField(max_length=500, blank=True)
    padre = models.ForeignKey(
        'self',
        verbose_name=u'ratón padre',
        related_name='hijos_de_padre',
        limit_choices_to={'sexo__iexact': 'M'},
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
    madre = models.ForeignKey(
        'self',
        verbose_name=u'ratona madre',
        related_name='hijos_de_madre',
        limit_choices_to={'sexo__iexact': 'F'},
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
    marca = models.CharField(max_length=300, blank=True, null=True)
    ubicacion = models.CharField(
        verbose_name=u"ubicación",
        max_length=300,
        blank=True,
        null=True)

    class Meta:
        verbose_name = u'ratón'
        verbose_name_plural = u'ratones'

    def __unicode__(self):
        return u'camada {0}; número {1}'.format(self.camada, self.numero)

    def get_absolute_url(self):
        return "/vivero/ratones/{0}".format(self.pk)

    def edad(self):
        delta = datetime.date.today() - self.nacimiento
        if not self.vive() and self.muerte is not None:
            delta = self.muerte - self.nacimiento
        if delta.days > 30:
            return u'{0} meses {1} días'.format(delta.days/30, delta.days%30)
        else:
            return u'{0} días'.format(delta.days)

    def sexo_verbose(self):
        if self.sexo == 'F':
            return 'femenino'
        else:
            return 'masculino'

    def estado_verbose(self):
        return dict(self.estados)[self.estado].lower()

    def vive(self):
        return self.estado == 'V' or self.estado == 'A' or self.estado == 'E'

    def reservado(self):
        hoy = datetime.date.today()
        return self.reserva_set.\
            filter(fecha_termino__isnull=False, fecha_termino__gt=hoy).\
            count() > 0 or self.reserva_set.\
            filter(fecha_termino__isnull=True, fecha__gte=hoy).\
            count() > 0

    def reservado_verbose(self):
        if self.reservado():
            return "si"
        return "no"
    reservado_verbose.short_description = u"¿reservado?"

    def reservable(self):
        return self.estado == 'V' and not self.reservado()

    def historicos(self):
        return self.historico_set.all()

    # Metodos de exportacion csv
    def get_csv_pairs(self):
        id_or_nothing = lambda obj: str(obj.id) if obj is not None else ""
        unicode_or_nothing = lambda obj: unicode(obj) if obj is not None else u""
        return [
            ("id", self.id),
            (u"línea genética", unicode(self.linea)),
            ("camada", self.camada),
            (u"número", self.numero),
            ("colonia", self.colonia),
            ("sexo", self.sexo),
            ("fecha de nac.", self.nacimiento.isoformat()),
            ("genotipo", unicode_or_nothing(self.genotipo)),
            ("regenotipo", unicode_or_nothing(self.regenotipo)),
            ("estado", self.estado_verbose()),
            (u"¿reservado?", self.reservado()),
            ("observaciones", self.observaciones),
            ("fecha de muerte", self.muerte),
            ("padre (id)", id_or_nothing(self.padre)),
            ("madre (id)", id_or_nothing(self.madre))]

    # Metodos de exportacion pdf
    def get_pdf_pairs(self):
        booleans = {True: "Si", False: "No"}
        return [
            (u"Identificación", unicode(self)),
            (u"Línea genética", self.linea),
            (u"Sexo", self.sexo_verbose()),
            (u"Genotipo", self.genotipo),
            (u"Regenotipo", self.regenotipo),
            (u"Edad", self.edad),
            (u"Estado", self.estado_verbose()),
            (u"¿Reservado?", booleans[self.reservado()]),
            (u"Colonia", self.colonia)]


class Reserva(models.Model, CSVExportable, PDFExportable):
    "Reservas de ratones"

    raton = models.ForeignKey(Raton, verbose_name=u'ratón')
    usuario = models.ForeignKey(User, verbose_name=u'usuario que reserva')
    tipos = (
        (u'T', u'Temporal'),
        (u'F', u'Terminal'),)
    tipo = models.CharField(
        verbose_name='tipo de reserva',
        max_length=1,
        default='F',
        choices=tipos)
    fecha = models.DateField(verbose_name='fecha de reserva')
    fecha_termino = models.DateField(
        verbose_name=u'fecha de término',
        blank=True,
        null=True)
    creada = models.DateTimeField(auto_now=True)
    observaciones = models.TextField(max_length=500, blank=True)

    def __unicode__(self):
        return u'{0} para {1}'.format(self.raton, self.fecha)

    def edad_reserva(self):
        delta = self.fecha - self.raton.nacimiento
        if delta.days > 30:
            return u'{0} meses {1} días'.format(delta.days/30, delta.days%30)
        return u'{0} días'.format(delta.days)
    edad_reserva.short_description = u"edad al momento de la reserva"

    def tipo_verbose(self):
        if self.tipo == 'T':
            return "temporal"
        return "terminal"

    # Metodos de exportacion csv
    def get_csv_pairs(self):
        return [
            ("id", self.id),
            (u"ratón", unicode(self.raton)),
            ("usuario", unicode(self.usuario)),
            ("tipo", self.tipo_verbose()),
            ("fecha", self.fecha.isoformat()),
            ("creada", self.creada.isoformat()),
            ("observaciones", self.observaciones),
            ("edad reserva", self.edad_reserva())]

    # Metodos de exportacion pdf
    def get_pdf_pairs(self):
        return [
            (u"Fecha", self.fecha),
            (u"Ratón", self.raton),
            (u"Usuario", self.usuario),
            (u"Tipo", self.tipo_verbose()),
            (u"Observaciones", self.observaciones)]


class Revision(models.Model, CSVExportable, PDFExportable):
    "Revisión veterinaria"

    raton = models.ForeignKey(Raton, verbose_name=u'ratón')
    fecha = models.DateField()
    peso = models.IntegerField(verbose_name='peso (gramos)')
    aspecto = models.TextField(max_length=500)
    choices3 = tuple(map(lambda x: (x, str(x)), range(4)))
    aspecto_puntaje = models.IntegerField(
        verbose_name='puntaje de aspecto',
        choices=choices3)
    comportamiento = models.TextField(
        verbose_name=u'comportamiento espontáneo',
        max_length=500)
    comportamiento_puntaje = models.IntegerField(
        verbose_name=u'puntaje de comportamiento espontáneo',
        choices=choices3)
    signos = models.TextField(
        verbose_name=u'signos neurológicos',
        max_length=500)
    signos_puntaje = models.IntegerField(
        verbose_name=u'puntaje de signos neurológicos',
        choices=choices3)
    constantes = models.TextField(
        verbose_name='constantes vitales',
        max_length=500)
    constantes_puntaje = models.IntegerField(
        verbose_name='puntaje de constantes vitales',
        choices=choices3)

    class Meta:
        verbose_name = u'revisión veterinaria'
        verbose_name_plural = u'revisiones veterinarias'

    def __unicode__(self):
        return u'revisión de ratón<{0}>'.format(self.raton)

    def get_absolute_url(self):
        return "/vivero/revisiones/{0}/".format(self.pk)

    def puntaje(self):
        return self.aspecto_puntaje + self.comportamiento_puntaje + \
            self.signos_puntaje + self.constantes_puntaje

    def get_csv_pairs(self):
        return [
            (u"fecha", self.fecha.isoformat()),
            (u"ratón", unicode(self.raton)),
            (u"peso (gramos)", self.peso),
            (u"puntaje", self.puntaje),
            (u"aspecto", self.aspecto_puntaje),
            (u"comportamiento espontáneo", self.comportamiento_puntaje),
            (u"signos neurológicos", self.signos_puntaje),
            (u"constantes vitales", self.constantes_puntaje)]

    def get_pdf_pairs(self):
        return [
            (u"Fecha", self.fecha),
            (u"Ratón", self.raton),
            (u"Peso (gramos)", self.peso),
            (u"Puntaje total de revisión", self.puntaje)]


# Archivos multimedia
def get_image_path(instance, filename):
    return "ratones/imagenes/{0}/{1}".format(instance.raton.id, filename)


class ImagenRaton(models.Model):
    raton = models.ForeignKey(Raton)
    imagen = models.ImageField(upload_to=get_image_path)
    fecha = models.DateField()
    descripcion = models.TextField(
        verbose_name=u"descripción",
        max_length=1000,
        blank=True)

    class Meta:
        verbose_name = u'imagen'
        verbose_name_plural = u'imágenes'

    def __unicode__(self):
        return u"imagen {0} de raton {1}".format(self.id, self.raton)


def get_video_path(instance, filename):
    return "ratones/videos/{0}/{1}".format(instance.raton.id, filename)

class VideoRaton(models.Model):
    raton = models.ForeignKey(Raton)
    video = models.FileField(upload_to=get_video_path)
    fecha = models.DateField()
    descripcion = models.TextField(
        verbose_name=u"descripción",
        max_length=1000,
        blank=True)

    class Meta:
        verbose_name = u'video'
        verbose_name = u'videos'

    def __unicode__(self):
        return u"video {0} de raton {1}".format(self.id, self.raton)


class Historico(models.Model):
    "Historico a desplegar en el administrador de ratones"

    raton = models.ForeignKey(Raton)
    instante = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1)
    evento = models.CharField(max_length=30) # reserva, revision, etc.
    usuario = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return u"histórico de {0}".format(self.raton)

    def estado_verbose(self):
        return dict(self.raton.estados)[self.estado]


# Señales de cambio de estado de ratones
# Obsoleto -- estado 'A' reservado para reservas
#@receiver(post_save, sender=Revision)
#def post_revision(sender, **kwargs):
#    revision = kwargs['instance']
#    if revision.fecha == datetime.date.today():
#        raton = revision.raton
#        if raton.estado == 'V':
#            raton.estado = 'A'
#            raton.save()

@receiver(post_save, sender=Reserva)
def post_reserva(sender, **kwargs):
    hoy = datetime.date.today()
    reserva = kwargs['instance']
    raton = reserva.raton
    if raton.estado != 'S' and raton.estado != 'M':
        if reserva.fecha <= hoy and reserva.tipo == 'F':
            raton.estado = 'S'
            raton.muerte = reserva.fecha
            raton.save()
        else:
            raton.estado = 'A'
            raton.save()
    # registrar reserva en historico
    h = Historico()
    h.raton = raton
    h.estado = raton.estado
    h.evento = u"reserva"
    h.usuario = reserva.usuario
    h.save()
