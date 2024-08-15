from django.contrib import admin
from applocaliza.models import Cliente, Vehiculo, empleado, reserva

# Register your models here.
admin.site.register(Cliente)
admin.site.register(empleado)
admin.site.register(Vehiculo)
admin.site.register(reserva)