from django.shortcuts import render
from django.http import HttpResponse

from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {
        'pets':pets,
    })
    #return HttpResponse('<p>home</p>')

def pet_detail(request, pet_id):
    
    #return HttpResponse(f'<p>pet_detail view with id {pet_id}</p>')