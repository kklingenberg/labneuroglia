# -*- coding: utf-8 -*-
from django.shortcuts import render
from pacientes.models import Paciente, EvaluacionMotora, EvaluacionFuncional, ExamenSignosVitales, ExamenFisico, ExamenNeurologico
from django.contrib.auth.decorators import login_required
from laboratorio.views import export_things_csv, export_things_pdf
from descriptores.models import Descripcion

@login_required
def index(request):
    descripcion = Descripcion.objects.filter(target="pacientes", enabled=True)
    descripcion = descripcion[0].body_to_html() \
        if descripcion else u"<p>No hay información</p>"
    return render(request, 'pacientes/index.html', {"description": descripcion})

# Exportar cosas en formato csv
@login_required
def export_pacientes_csv(request):
    return export_things_csv(request, Paciente, 'pacientes.csv')

@login_required
def export_pacientes_pdf(request):
    return export_things_pdf(request, Paciente, 'pacientes.csv', "pacientes")

@login_required
def export_evalmotoras_csv(request):
    return export_things_csv(request, EvaluacionMotora, 'evalmotoras.csv')

@login_required
def export_evalmotoras_pdf(request):
    return export_things_pdf(request, EvaluacionMotora, 'evalmotoras.pdf', "evaluaciones motoras")

@login_required
def export_evalfunc_csv(request):
    return export_things_csv(request, EvaluacionFuncional, 'evalfuncionales.csv')

@login_required
def export_evalfunc_pdf(request):
    return export_things_pdf(request, EvaluacionFuncional, 'evalfuncionales.pdf', "evaluaciones funcionales")

@login_required
def export_esignosvitales_csv(request):
    return export_things_csv(request, ExamenSignosVitales, 'signosvitales.csv')

@login_required
def export_efisico_csv(request):
    return export_things_csv(request, ExamenFisico, 'examenesfisicos.csv')

@login_required
def export_eneurologico_csv(request):
    return export_things_csv(request, ExamenNeurologico, 'examenesneurologicos.csv')

