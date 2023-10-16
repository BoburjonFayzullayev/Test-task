from django.contrib import admin
from .models import Appointment, Identifier

admin.site.register(Identifier)

admin.site.register(Appointment)