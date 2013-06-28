from django.core.management.base import BaseCommand
from vivero.models import Raton, Reserva, Revision, Historico
import datetime

class Command(BaseCommand):
    args = 'no arguments'
    help = 'register the deaths ocurred as a result of reservations'

    def handle(self, *args, **options):
        hoy = datetime.date.today()
        cont_a = 0
        cont_v = 0
        cont_s = 0
        # Obtener todas las revisiones que ocurriran hoy
        # y cambiar el estado de esos ratones
        # -------------------------------------------------------
        # Obsolteo -- el estado bajo analisis es exclusivo de las reservas T
        #revisiones = Revision.objects.filter(fecha=hoy)
        #for revision in revisiones:
        #    raton = revision.raton
        #    if raton.estado == 'V':
        #        raton.estado = 'A'
        #        raton.save()
        #        cont_a = cont_a + 1
        # Cambiar ratones marcados 'bajo analisis' a 'en vivero' si
        # no tienen revisiones o reservas temporales hoy
        # ---------------------------------------------------------
        # Obsoleto -- opte por dejarlos bajo analisis hasta que
        # mueran
        #ratones_ba = Raton.objects.filter(estado__iexact='A')
        #for raton in ratones_ba:
        #    if raton.revision_set.filter(fecha=hoy).count() == 0 and raton.reserva_set.filter(fecha=hoy, tipo__iexact='T').count() == 0:
        #        raton.estado = 'V'
        #        raton.save()
        #        cont_v = cont_v + 1
        # --------------------------------------------------------
        # Obtener todas las reservas que ocurriran hoy
        # y cambiar el estado de esos ratones
        reservas_f = Reserva.objects.filter(fecha=hoy, tipo='F')
        for reserva in reservas_f:
            raton = reserva.raton
            if raton.estado != 'S' and raton.estado != 'M':
                raton.estado = 'S'
                raton.muerte = reserva.fecha
                raton.save()
                cont_s = cont_s + 1
                # historico
                h = Historico()
                h.raton = raton
                h.estado = raton.estado
                h.usuario = reserva.usuario
                h.evento = "sacrificado"
                h.save()
        reservas_t = Reserva.objects.filter(fecha=hoy, tipo='T')
        for reserva in reservas_t:
            raton = reserva.raton
            if raton.estado == 'V':
                raton.estado = 'A'
                raton.save()
                cont_a = cont_a + 1
                # historico
                h = Historico()
                h.raton = raton
                h.estado = raton.estado
                h.usuario = reserva.usuario
                h.evento = "reserva"
                h.save()
        reservas_terminadas = Reserva.objects.filter(fecha_termino=hoy, tipo='T')
        for reserva in reservas_terminadas:
            raton = reserva.raton
            if raton.estado == 'A':
                raton.estado = 'V'
                raton.save()
                cont_v = cont_v + 1
                # historico
                h = Historico()
                h.raton = raton
                h.estado = raton.estado
                h.usuario = reserva.usuario
                h.evento = "fin reserva"
                h.save()

        self.stdout.write('{0} ocupados; {1} scarificados; {2} disponibles\n'.format(cont_a, cont_s, cont_v))

