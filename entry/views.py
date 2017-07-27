from django.shortcuts import render, get_object_or_404 as getOb
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Beer
# Create your views here.

def HomeView(request):
        return render(request, 'entry/home.html')
        
        
def makeSale(request):
    data = Beer.objects.all()
    return render(request, 'entry/sale.html', {'object_list':data})
    
def postSale(request, saleDat=None):
    
    #This is where the passed sale data gets input into the database
    for beer in saleDat:
        sale = getOb(Beer, pk= beer.id)
        
    return HttpResponseRedirect(reverse('entry:confirm'))
    