# -*- coding: utf-8 -*-
import re

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


make_sub = lambda char, regchar, opentag, closetag: lambda text: re.sub(
    "{0}(.*?){0}".format(regchar),
    lambda mobj: u"{0}{1}{2}".format(opentag, mobj.group(1), closetag) \
        if mobj.group(1) else char,
    text)


sub_bold = make_sub("*", "\*", u"<strong>", u"</strong>")
sub_italic = make_sub("_", "_", u"<em>", u"</em>")
sub_titles = make_sub("=", "=", u'<span style="font-size: 1.5em;">', u"</span>")


class Descripcion(models.Model):

    target_options = (
        ('global', u'sitio en general'),
        ('pacientes', u'pacientes'),
        ('viales', u'líneas celulares'),
        ('vivero', u'vivero'))
    target = models.CharField(
        verbose_name=u"módulo",
        max_length=20,
        choices=target_options,
        help_text=u"Módulo a describir")

    enabled = models.BooleanField(verbose_name=u"activado", default=True)

    body = models.TextField(
        verbose_name=u"Descripción del módulo",
        blank=True,
        help_text=u'<span style="font-size: 1.2em;">Escriba frases entre '\
            u'asteriscos (*) para que se muestren en negrita. '\
            u'Use guiones bajos (_) para que se muestren en cursiva. '\
            u'Use el signo igual (=) para títulos.<br />'\
            u'Si quiere usar alguno de esos símbolos, '\
            u'insértelo dos veces (e.g. **).</span>')

    class Meta:
        verbose_name = u"descripción de módulo"
        verbose_name_plural = u"descripciones de módulos"

    def __unicode__(self):
        return u"Descripción para {0}{1}{2}".format(
            dict(self.target_options)[self.target],
            u" MOSTRADO ACTUALMENTE" if self.enabled else u"",
            u": {0}...".format(self.body[:10]))

    def body_to_html(self):
        # split in paragraphs
        pars = self.body.split("\n")
        # sub titles
        pars = map(sub_titles, pars)
        # sub bold
        pars = map(sub_bold, pars)
        # sub italic
        pars = map(sub_italic, pars)
        return "".join(map(lambda p: u"<p>{0}</p>\n".format(p.strip()), pars))

@receiver(post_save, sender=Descripcion, dispatch_uid="set_rest_disabled")
def set_rest_disabled(sender, instance, **kwargs):
    if instance.enabled:
        Descripcion.objects.filter(
            ~models.Q(id=instance.id), enabled=True, target=instance.target).\
            update(enabled=False)
