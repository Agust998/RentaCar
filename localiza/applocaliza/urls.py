from django.urls import path, include
from applocaliza import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path("cliente/",views.Cliente),
    path("empleado/",views.empleado),
    path("reserva/",views.reserva),
    path("vehiculo/",views.vehiculo, name="vehiculo"),
    path('formapi1/', views.formapi1, name="FormApi1"),
    path('buscarvehiculo/', views.buscarvehiculo, name="buscarvehiculo")
]
