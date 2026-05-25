
from django.urls import path
from web.views import home,proyectos,contacto,calculadora_francos


urlpatterns = [
    path('',home, name='home'),
    path('proyectos/', proyectos, name='proyectos'),
    path('contacto/', contacto, name='contacto'),
    path('proyectos/calculadora', calculadora_francos, name='calculadora_francos')
]