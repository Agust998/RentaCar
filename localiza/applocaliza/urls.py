from django.urls import path, include
from applocaliza import views

urlpatterns = [
    path("",views.inicio),
    path("cliente/",views.cliente),
    path("empleado/",views.empleado),
    path("reserva/",views.reserva),
    path("vehiculo/",views.vehiculo),
]
