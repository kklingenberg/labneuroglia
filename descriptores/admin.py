from descriptores.models import Descripcion
from django.contrib import admin


class DescripcionAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'enabled', 'target')
    list_filter = ['target']

admin.site.register(Descripcion, DescripcionAdmin)
