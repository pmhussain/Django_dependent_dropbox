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


#AJAX functions
def loadstates(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country=country_id)
    print(states)
    context = {
    'states' : states,
    }
    return render (request, 'states_dropdown_list.html', context)


def loaddistricts(request):
    state_id = request.GET.get('state_id')
    districts = District.objects.filter(state=state_id)
    print(districts)
    context = {
    'districts' : districts,
    }
    return render (request, 'districts_dropdown_list.html', context)
