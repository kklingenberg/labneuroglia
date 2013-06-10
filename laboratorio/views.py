# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import loader, Context
from django.contrib.auth.decorators import login_required
from descriptores.models import Descripcion
import xhtml2pdf.pisa as pisa
import cStringIO as StringIO
import cgi

def home(request):
    descripcion = Descripcion.objects.filter(target="global")
    descripcion = descripcion[0].body_to_html() \
        if descripcion else u"<p>No hay información</p>"
    return render(request, 'home.html', {"description": descripcion})

@login_required
def backup(request):
    if request.user.is_superuser or request.user.groups.filter(name="superusuarios lab").count() > 0:
        response = HttpResponse(mimetype='text/plain')
        response['Content-Disposition'] = 'attachment; filename=respaldo.sql'
        t = loader.get_template('backup.sql')
        response.write(t.render(Context()))
        return response
    else:
        return HttpResponse("<p>No tienes permisos suficientes para descargar este archivo.</p>")

# Exportar conjunto de datos en formato csv
def export_csv(header, dataset, filename):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)

    t = loader.get_template('export_csv.txt')
    c = Context({
        'header': header,
        'dataset': dataset
    })
    response.write(t.render(c))
    return response

# Exportar objetos en formato csv
def export_things_csv(request, thing, filename):
    ids = []
    try:
        ids = request.GET['ids'].split(',')
    except KeyError:
        pass

    things = thing.objects.all()
    if ids:
        things = things.filter(pk__in=ids)
    header = []
    dataset = []
    if things.count() > 0:
        header = things[0].get_header()
        dataset = map(lambda x: x.get_row(), things)

    return export_csv(header, dataset, filename)

# Exportar plantilla a pdf
def render_to_pdf(template_src, context_dict=None, filename='document.pdf'):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
        return response
    return HttpResponse("Hubieron problemas al generar el documento<pre>%s</pre>" % cgi.escape(html))

# Exportart conjunto de datos a pdf
def export_things_pdf(request, thing, filename, desc):
    ids = []
    try:
        ids = request.GET['ids'].split(',')
    except KeyError:
        pass

    things = thing.objects.all()
    if ids:
        things = things.filter(pk__in=ids)
    header = []
    dataset = []
    if things.count() > 0:
        header = things[0].get_pdfheader()
        dataset = map(lambda x: x.get_pdfrow(), things)

    return render_to_pdf('export_pdf.html',
        {
            'header': header,
            'dataset': dataset,
            'data_descriptor': desc
        }, filename)

