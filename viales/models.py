from django.db import models
from django.contrib.auth.models import User
import datetime
from exportable import CSVExportable, PDFExportable

# Refrigeradores o contenedores
class Stock(models.Model):
    nombre = models.CharField(verbose_name='nombre', max_length=100)
    descripcion = models.TextField(verbose_name=u'descripci\u00F3n', max_length=250, blank=True)
    def __unicode__(self):
        return self.nombre

# Lineas celulares
class Linea(models.Model):
    nombre = models.CharField(verbose_name=u'l\u00EDnea celular', max_length=50)
    descripcion = models.TextField(verbose_name=u'descripci\u00F3n adicional', max_length=250, blank=True)
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        verbose_name = u'l\u00EDnea celular'
        verbose_name_plural = u'l\u00EDneas celulares'

# Viales congelados
class Vial(models.Model, CSVExportable, PDFExportable):
    ubicacion = models.CharField(verbose_name=u'ubicaci\u00F3n', max_length=20, blank=True)
    fecha = models.DateField(u'fecha de congelaci\u00F3n')
    linea = models.ForeignKey(Linea, verbose_name=u"l\u00EDnea celular")
    stock = models.ForeignKey(Stock)
    op_vigente = (
        (u'S', u'S\u00ED'),
        (u'N', u'No'),
    )
    vigente = models.CharField(verbose_name=u'\u00BFvigente?', max_length=1, default='S', choices=op_vigente, help_text=u'Selecciona \"No\" para indicar que el vial fue usado.')
    observaciones = models.TextField(verbose_name="observaciones", max_length=500, blank=True)
    usuario = models.ForeignKey(User, verbose_name="usuario que congela")
    descongelacion = models.DateField(verbose_name=u'fecha de descongelaci\u00F3n', null=True, blank=True)
    usuario_descongela = models.ForeignKey(User, verbose_name="usuario que descongela", null=True, blank=True, related_name='descongelo_viales')

    def __unicode__(self):
        return u'vial {0} de l\u00EDnea {1}'.format(self.ubicacion, self.linea.nombre)
    def congelado_hoy(self):
        return self.fecha == datetime.date.today()
    def fue_descongelado(self):
        return self.vigente == 'N'
    def fecha_descongelacion(self):
        if self.descongelacion is None:
            return "<no ha sido descongelado>"
        else:
            return self.descongelacion.isoformat()
    def descongelado_por(self):
        if self.usuario_descongela is None:
            return u'<nadie todav\u00EDa>'
        else:
            return self.usuario_descongela

    # Metodos de exportacion
    def get_csv_pairs(self):
        return [
            ("id",                            self.id),
            (u"l\u00EDnea",                   self.linea.nombre),
            ("stock",                         self.stock.nombre),
            (u"ubicaci\u00F3n",               self.ubicacion),
            (u"fecha de congelaci\u00F3n",    self.fecha.isoformat()),
            ("vigente",                       self.vigente),
            (u"congelado por",                self.usuario.__unicode__()),
            ("observaciones",                 self.observaciones),
            (u"fecha de descongelaci\u00F3n", self.fecha_descongelacion()),
            (u"descongelado por",             self.descongelado_por())
        ]

    def get_pdf_pairs(self):
        return [
            (u"L\u00EDnea",     self.linea),
            (u"Stock",          self.stock),
            (u"Ubicaci\u00F3n", self.ubicacion),
            (u"Congelado",      self.fecha),
            (u"Por",            self.usuario),
            (u"Descongelado",   self.fecha_descongelacion()),
            (u"Por",            self.descongelado_por())
        ]

    class Meta:
        verbose_name_plural = "viales"

