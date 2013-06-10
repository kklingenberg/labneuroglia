# -*- coding: utf-8 -*-
import re

from django.db import models


sub_bold = lambda text: re.sub(
    "\*(.*?)\*",
    lambda mobj: u"<strong>{0}</strong>".format(mobj.group(1)),
    text)

sub_italic = lambda text: re.sub(
    "_(.*?)_",
    lambda mobj: u"<em>{0}</em>".format(mobj.group(1)),
    text)

sub_titles = lambda text: re.sub(
    "=(.*?)=",
    lambda mobj: u'<span style="font-size: 1.5em;">{0}</span>'.\
        format(mobj.group(1)),
    text)


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

    body = models.TextField(
        verbose_name=u"Descripción del módulo",
        blank=True,
        help_text=u"Escriba frases entre asteriscos (*) para que se muestren "\
            u"en negrita. Use guiones bajos (_) para que se muestren "\
            u"en cursiva. Use el signo igual (=) para títulos.")

    class Meta:
        verbose_name = u"descripción de módulo"
        verbose_name_plural = u"descripciones de módulos"

    def __unicode__(self):
        return u"Descripción para {0}".format(dict(self.target_options)[self.target])

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
