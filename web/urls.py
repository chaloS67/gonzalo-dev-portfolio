
from django.urls import path
from web.views import home,proyectos,contacto


urlpatterns = [
    path('',home, name='home'),
    path('proyectos/', proyectos, name='proyectos'),
    path('contacto/', contacto, name='contacto'),
]