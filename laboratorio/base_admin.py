"""
View-permission aware admin.
Based on: http://gremu.net/blog/2010/django-admin-read-only-permission/
"""

from django.core.exceptions import PermissionDenied
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType


class BaseAdmin(admin.ModelAdmin):
    def has_view_permission(self, request):
        model = self.model
        ct = ContentType.objects.get_for_model(model)
        return request.user.has_perm('{0}.view_{1}'.format(
                model._meta.app_label, model.__name__.lower()))

    def get_model_perms(self, request):
        perms = super(BaseAdmin, self).get_model_perms(request)
        perms['change'] = perms['view'] = self.has_view_permission(request)
        return perms

    def has_change_permission(self, request, obj=None):
        if getattr(request, 'readonly', False):
            return True
        return super(BaseAdmin, self).has_change_permission(request, obj)

    def changelist_view(self, request, extra_context=None):
        try:
            return super(BaseAdmin, self).changelist_view(
                request, extra_context=extra_context)
        except PermissionDenied:
            pass
        if request.method == 'POST':
            raise PermissionDenied
        if self.has_view_permission(request):
            request.readonly = True
        return super(BaseAdmin, self).changelist_view(
            request, extra_context=extra_context)

    def change_view(self, request, object_id, extra_context=None):
        try:
            return super(BaseAdmin, self).change_view(
                request, object_id, extra_context=extra_context)
        except PermissionDenied:
            pass
        if request.method == 'POST':
            raise PermissionDenied
        if self.has_view_permission(request):
            request.readonly = True
        return super(BaseAdmin, self).change_view(
            request, object_id, extra_context=extra_context)
