from django.contrib import admin
from locations.models import Department, City, Neighborhood

# Register your models here.

admin.site.register(Department)
admin.site.register(City)
admin.site.register(Neighborhood)