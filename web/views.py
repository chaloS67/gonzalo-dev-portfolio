import datetime
from django.shortcuts import render
import locale


def home (request):
    return render(request,'web/home.html')

def proyectos (request):
    return render(request,'web/proyectos.html')

def contacto (request):
    return render(request,'web/contacto.html')

def calcular_francos(fecha_inicio,cantidad_francos):
   
    resultados = []
    año_inicio = fecha_inicio.year

    while fecha_inicio.year == año_inicio: # mientras sea dentro del mismo año

        if cantidad_francos == 1:
           
            franco_1 = fecha_inicio + datetime.timedelta(days=7) # CALCULA PRIMER FRANCO 6 dias trabajados 
            franco_2= fecha_inicio + datetime.timedelta(days=8)
        
        
            resultados.append(franco_1)
            resultados.append(franco_2)

            fecha_inicio = franco_2 
            cantidad_francos = 2 # establesco la cantidad de francos para que entre en el siguiente

        else:
      
            
            franco = fecha_inicio + datetime.timedelta(days=7)# aigno la la fecha
           
            resultados.append(franco)
       
            fecha_inicio= franco # establesco la fecha luego de mi franco
            cantidad_francos = 1 # establesco la cantidad de franco siguientes

    return resultados

def calculadora_francos(request):

    francos = []
    error = None
    if request.method == "POST":

        fecha_texto = request.POST.get("fecha")
        cantidad = request.POST.get("cantidad")

        try:
            
            fecha_inicio = datetime.datetime.strptime(fecha_texto, "%Y-%m-%d").date()
            cantidad_francos = int(cantidad)
            francos = calcular_francos(fecha_inicio, cantidad_francos)
        
        except ValueError:
            error = "Error ingresa una fecha valida"


    return render(request,'web/calculadora_francos.html',
                  {
                      "francos": francos,
                      "error" : error
                  })
