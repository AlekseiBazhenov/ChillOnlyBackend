from django.contrib import admin

from app.models import Station


class StationAdmin(admin.ModelAdmin):
    list_display = ('title', 'station_url', 'created', 'updated')
    search_fields = ('title',)


admin.site.register(Station, StationAdmin)
