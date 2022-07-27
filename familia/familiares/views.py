from django.shortcuts import render

from familiares.models import Familiares

def crear_familiar(request):
    new_familiar = Familiares.objects.create(name = 'Andrea', age = 40, description = 'Hermana')
    context ={
        'new_familiar':new_familiar
    }
    return render(request, 'new_familiar.html', context=context)

def list_familiares(request):
    familiares = Familiares.objects.all()
    context={
        'familiares':familiares
    }
    return render (request, 'familiares_list.html', context=context)