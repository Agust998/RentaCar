from django.shortcuts import render, redirect
from django.http import HttpResponse
from applocaliza.forms import registroFormulario
from applocaliza.models import Cliente, Vehiculo
from applocaliza.forms import buscarAuto

def inicio(request) :
    return render(request, "applocaliza/base.html")

def cliente(request) :
    return HttpResponse("vista cliente")

def empleado(request) :
    return HttpResponse("vista empleado")

def reserva(request) :
    return HttpResponse("vista reserva")

def vehiculo(request) :
    return render(request, "applocaliza/index.html")

def formapi1(request):

    if request.method == "POST":
        mi_formulario = registroFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            cliente = Cliente(
                            nombre=informacion["nombre"], 
                            apellido=informacion["apellido"], 
                            email=informacion ["email"], 
                            password=informacion["password"]
                            )
            cliente.save()
            

            return render(request,"applocaliza/index.html")
        else:
            # Si el formulario no es válido, se renderiza de nuevo con el formulario
            return render(request, "applocaliza/formapi1.html", {"mi_formulario": mi_formulario})
        
    else:
        mi_formulario = registroFormulario()

    return render(request, "applocaliza/formapi1.html", {"mi_formulario": mi_formulario})

def buscarvehiculo(request):
    if request.method == "POST":
        mi_formulario = buscarAuto(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            auto = Vehiculo.objects.filter(marca__icontains=informacion["auto"])

            return render(request, "applocaliza/mostrarvehiculo.html", {"auto": auto} )
    else:
        mi_formulario = buscarAuto()

    return render(request, "applocaliza/buscarvehiculo.html",{"mi_formulario": mi_formulario})