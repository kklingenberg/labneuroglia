from django.shortcuts import render_to_response
from viales.models import Stock, Linea, Vial
from django.contrib.auth.decorators import login_required
import datetime
from labs.views import export_things_csv, export_things_pdf

@login_required
def index(request):
    stocks = Stock.objects.all()
    lineas = Linea.objects.all()
    viales = dict(map(lambda s: (s.nombre, dict(map(lambda l: (l.nombre, l.vial_set.filter(stock=s, vigente__iexact='S').count()), lineas))), stocks))
    total = sum(map(lambda c: sum(c.values()) , viales.values()))
    return render_to_response('viales/index.html', {'viales': viales, 'total': total})

@login_required
def lastmonth(request):
    today = datetime.date.today()
    viales = Vial.objects.filter(fecha__gte=today-datetime.timedelta(30)).order_by('-fecha')
    return render_to_response('viales/lastmonth.html', {'viales': viales})

@login_required
def log(request):
    viales = Vial.objects.filter(vigente__iexact='N').order_by('-fecha')
    return render_to_response('viales/log.html', {'viales': viales})

# Exportar viales en formato csv
@login_required
def export_viales_csv(request):
    return export_things_csv(request, Vial, 'viales.csv')

# En pdf
@login_required
def export_viales_pdf(request):
    return export_things_pdf(request, Vial, 'viales.pdf', "viales")

