from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    countries = Country.objects.all()
    states = State.objects.none()
    districts =  District.objects.none()
    context = {
    'countries' : countries,
    'states' : states,
    'districts' : districts,
    }
    return render (request, 'home.html',context)

def loadstates(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country=country_id)
    print(states)
    context = {
    'states' : states,
    }
    return render (request, 'states_dropdown_list.html', context)
