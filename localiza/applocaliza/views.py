from django.shortcuts import render
from django.http import HttpResponse

def inicio(request) :
    return HttpResponse("vista inicio")

def cliente(request) :
    return HttpResponse("vista cliente")

def empleado(request) :
    return HttpResponse("vista empleado")

def reserva(request) :
    return HttpResponse("vista reserva")

def vehiculo(request) :
    return HttpResponse("vista vehiculo")