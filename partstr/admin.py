from django.contrib import admin

# Register your models here.
from .models import Part, Level, Status, PnType

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['partnumber','designation','status','level','parent', 'resp', 'created', 'updated']
    search_fields = ['partnumber', 'status']

# visible tables from admin site
admin.site.register(Level)
admin.site.register(Status)
admin.site.register(PnType)