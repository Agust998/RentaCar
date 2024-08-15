from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from applocaliza.models import Cliente

class clienteListview(ListView) :
    model = Cliente
    context_object_name = "cliente"
    template_name = "empleado/vista_cliente.html"