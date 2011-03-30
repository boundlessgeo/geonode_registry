from django.contrib import admin
from registry.models import GeoNode

class GeoNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'layer_count', 'map_count')

admin.site.register(GeoNode, GeoNodeAdmin)
