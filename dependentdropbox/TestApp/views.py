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



#Without AJAX
def withoutajax(request):
    countries = Country.objects.all()
    country_id = request.GET.get('country_id', None)
    state_id = request.GET.get('state_id', None)
    states = None
    districts = None
    print(locals())
    if country_id:
        get_country = Country.objects.get(id=country_id)
        states = State.objects.filter(country=get_country)
        print(states)
    if state_id:
        get_state = State.objects.get(id=state_id)
        districts = District.objects.filter(state=get_state)
        print(districts)
    context = {
    'countries' : countries,
    'states' : states,
    'districts' : districts,
    }
    return render (request, 'withoutajax.html',locals())
