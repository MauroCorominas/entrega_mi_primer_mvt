
from django.contrib import admin
from django.urls import path
from familia.views import saludo
from familiares.views import crear_familiar,list_familiares

urlpatterns = [
    path('admin/', admin.site.urls),

    path('saludo/',saludo,name='saludo'),
    path('crear-familiar/',crear_familiar,name='crear_familiar'),
    path('lista-familiares/',list_familiares,name='list_familiares'),
]
