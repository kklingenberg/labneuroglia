from django.shortcuts import render_to_response
from pacientes.models import Paciente, EvaluacionMotora, EvaluacionFuncional, ExamenSignosVitales, ExamenFisico, ExamenNeurologico
from django.contrib.auth.decorators import login_required
from views import export_things_csv, export_things_pdf

@login_required
def index(request):
    return render_to_response('pacientes/index.html')

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

