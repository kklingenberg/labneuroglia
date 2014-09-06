from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from vivero.models import *
from laboratorio.views import export_things_csv, export_things_pdf
import datetime
import math

@login_required
def index(request):    
    ratones = Raton.objects.exclude(estado__iexact='S').exclude(estado__iexact='M').exclude(estado__iexact='E').order_by('linea', 'camada', 'numero')
    total = ratones.count()
    return render(request, 'vivero/index.html', {'ratones': ratones, 'total': total})

# Detalle de raton
@login_required
def detail(request, raton_id):
    raton = get_object_or_404(Raton, pk=raton_id)
    reservas = raton.reserva_set.order_by('creada')
    revisiones = raton.revision_set.order_by('fecha')
    return render(request, 'vivero/detail.html', {'raton': raton, 'reservas': reservas, 'revisiones': revisiones})

# Exportar ratones en formato csv
@login_required
def export_ratones_csv(request):
    return export_things_csv(request, Raton, 'ratones.csv')

# en formato pdf
@login_required
def export_ratones_pdf(request):
    return export_things_pdf(request, Raton, 'ratones.pdf', "ratones")

@login_required
def export_reservas_csv(request):
    return export_things_csv(request, Reserva, 'reservas.csv')

@login_required
def export_reservas_pdf(request):
    return export_things_pdf(request, Reserva, 'reservas.pdf', "reservas")

@login_required
def export_revisiones_csv(request):
    return export_things_csv(request, Revision, 'revisiones.csv')

@login_required
def export_revisiones_pdf(request):
    return export_things_pdf(request, Revision, 'revisiones.pdf', "revisiones veterinarias")

# Reservar raton
@login_required
def reserve(request, raton_id):
    raton = get_object_or_404(Raton, pk=raton_id)
    prev = None
    try:
        prev = request.GET['prev'] # para redirigir
    except KeyError:
        pass
    try:
        tipo = request.POST['tipo']
        observaciones = request.POST['observaciones']
        parts = request.POST['fecha'].rsplit('/')
        fecha = datetime.date(int(parts[2]), int(parts[1]), int(parts[0]))
        fecha_t = None
        if tipo == "T":
            parts_t = request.POST['fechat'].rsplit('/')
            fecha_t = datetime.date(int(parts_t[2]), int(parts_t[1]), int(parts_t[0]))
    except KeyError:
        return render(request, 'vivero/reserve.html', {
            'raton': raton,
            'error_message': u'Error al reservar rat\u00F3n. Se cancel\u00F3 la reserva.',
            'prev': prev,
        })
    except (IndexError, ValueError):
        return render(request, 'vivero/reserve.html', {
            'raton': raton,
            'error_message': u"Fecha inv\u00E1lida.",
            'prev': prev,
        })
    else:
        reserva = Reserva()
        reserva.raton = raton
        reserva.usuario = request.user
        reserva.tipo = tipo
        reserva.fecha = fecha
        if tipo == "T":
            reserva.fecha_termino = fecha_t
        reserva.observaciones = observaciones
        reserva.save()
        if prev is None:
            return HttpResponseRedirect(reverse('vivero.views.detail', args=(raton.id,)))
        else:
            return HttpResponseRedirect(prev)

# Formulario de reserva
@login_required
def reservationform(request, raton_id):
    raton = get_object_or_404(Raton, pk=raton_id)
    prev = None # la vista anterior, usada para redirigir al administrador
    try:
        prev = request.GET['prev']
    except KeyError:
        pass
    return render(request, 'vivero/reserve.html', {'raton': raton, 'prev': prev})

# Revision de un raton
@login_required
def revision(request, revision_id):
    revision = get_object_or_404(Revision, pk=revision_id)
    return render(request, 'vivero/revision.html', {'revision': revision})

# Reservas efectuadas desde un mes atras
@login_required
def reservations(request):
    hoy = datetime.date.today()
    reservas = map(lambda f: (f['fecha'], Reserva.objects.filter(fecha=f['fecha'])), Reserva.objects.filter(fecha__gt=hoy-datetime.timedelta(30)).order_by('fecha').values('fecha').distinct())
    return render(request, 'vivero/reservations.html', {'reservas': reservas})

# Bitacora de ratones sacrificados y muertos
@login_required
def log(request):
    ratones = Raton.objects.filter(Q(estado__iexact='S') | Q(estado__iexact='M') | Q(estado__iexact='E')).order_by('-nacimiento')
    total = ratones.count()
    return render(request, 'vivero/log.html', {'ratones': ratones, 'total': total})

# Histograma de muertes
@login_required
def histogram(request):
    hoy = datetime.date.today()
    response = {'hasta': hoy.strftime("%d/%m/%Y")}
    queryfilter = Q(estado__iexact='M')
    try:
        def parsedate(d):
            try:
                parts = d.split('/')
                return datetime.date(int(parts[2]), int(parts[1]), int(parts[0]))
            except (ValueError, IndexError):
                return None
        desde = parsedate(request.GET['desde'])
        hasta = parsedate(request.GET['hasta'])
        if not (desde is None):
            queryfilter = queryfilter & Q(nacimiento__gte=desde)
            response['desde'] = desde.strftime("%d/%m/%Y")
        if not (hasta is None):
            queryfilter = queryfilter & Q(nacimiento__lte=hasta)
            response['hasta'] = hasta.strftime("%d/%m/%Y")
    except KeyError:
        queryfilter = queryfilter & Q(nacimiento__lte=hoy)
    ratones = Raton.objects.filter(queryfilter)
    genotipos = map(lambda x: x['genotipo__genotipo'], ratones.values('genotipo__genotipo').distinct())
    lineas = map(lambda x: x['linea__linea'], ratones.values('linea__linea').distinct())
    conjunto = map(lambda x: {'tiempo': (x.muerte - x.nacimiento).days, 'genotipo': x.genotipo.genotipo, 'sexo': x.sexo, 'linea': x.linea.linea}, ratones)
    conjunto.sort(key=lambda y: y['tiempo'])
    total = len(conjunto)
    if total == 0:
        return render(request, 'vivero/histogram.html', {'total': 0})
    k = math.ceil(1 + math.log(total, 2))
    if k < 6:
        k = 6.0
    edadmax = conjunto[-1]['tiempo']
    edadmin = conjunto[0]['tiempo']
    rango = edadmax - edadmin
    clases = [edadmin + i*rango*1.0/k for i in range(int(k))]
    def doseries(selector, labels, classes, rawset):
        series = []
        for label in labels:
            data = []
            for i in range(len(classes)):
                if i == len(classes) - 1:
                    data.append([classes[i], len(filter(lambda x: x[selector] == label and x['tiempo'] >= classes[i], rawset))])
                else:
                    data.append([classes[i], len(filter(lambda x: x[selector] == label and x['tiempo'] >= classes[i] and x['tiempo'] < classes[i+1], rawset))])
            series.append({'label': label, 'data': data})
        return series
    response['series_genotipo'] = doseries('genotipo', genotipos, clases, conjunto)
    response['series_sexo'] = doseries('sexo', ['M', 'F'], clases, conjunto)
    response['series_linea'] = doseries('linea', lineas, clases, conjunto)
    response['amplitud'] = str(rango*1.0/k)
    response['total'] = total
    return render(request, 'vivero/histogram.html', response)
