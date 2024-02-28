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
    if request.method == 'POST':
        print(request.POST)
        country_id =int(request.POST.get('country'))
        state_id = int(request.POST.get('state'))
        district_id = int(request.POST.get('district'))
        print(type(country_id),country_id)
        name = request.POST.get('name')
        country = Country.objects.get(id=country_id)
        state = State.objects.get(id=state_id)
        district = District.objects.get(id=district_id)
        person = Person(name=name,country=country,state=state, district=district)
        person.save()
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
    country = request.GET.get('country', None)
    state = request.GET.get('state', None)
    states = None
    districts = None
    print(locals())
    if country:
        get_country = Country.objects.get(name=country)
        states = State.objects.filter(country=get_country)
        print(states)
    if state:
        get_state = State.objects.get(name=state)
        districts = District.objects.filter(state=get_state)
        print(districts)
    context = {
    'countries' : countries,
    'states' : states,
    'districts' : districts,
    }
    return render (request, 'withoutajax.html',locals())
