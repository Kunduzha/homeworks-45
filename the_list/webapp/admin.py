from django.contrib import admin
from webapp.models import List

# Register your models here.
# class ListAdmin(admin.ModelAdmin):


class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'description', 'created_at', 'about_list']
    list_filter = ['description']
    search_fields = ['status', 'description']
    fields = ['id', 'status', 'description', 'created_at','about_list']
    readonly_fields = ['created_at', 'id']


admin.site.register(List, ListAdmin)