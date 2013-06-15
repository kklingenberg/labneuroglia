from descriptores.models import Descripcion
from laboratorio.base_admin import BaseAdmin
from django.contrib import admin


class DescripcionAdmin(BaseAdmin):
    list_display = ('__unicode__', 'enabled', 'target')
    list_filter = ['target']

admin.site.register(Descripcion, DescripcionAdmin)
