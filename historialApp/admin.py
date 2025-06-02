
from django.contrib import admin
from .models import Propietario, Mascota, ConsultaMedica

# Register your models here.

admin.site.register(Propietario)
admin.site.register(Mascota)
admin.site.register(ConsultaMedica)
