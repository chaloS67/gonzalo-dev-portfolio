from django.shortcuts import render

def home (request):
    return render(request,'web/home.html')

def proyectos (request):
    return render(request,'web/proyectos.html')

def contacto (request):
    return render(request,'web/contacto.html')
