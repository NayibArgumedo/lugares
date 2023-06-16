from django.contrib import admin
from pets.models import Person, Pets

# Register your models here.

admin.site.register(Person)
admin.site.register(Pets)