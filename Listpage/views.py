from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from Database.models import Property
from django.contrib.auth.models import User
from django.http import Http404
from django.views import View
from Listpage.choices import price_choices, bedroom_choices, bathroom_choices, parking_choices, sort_choices
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'listpage.html')

def detailspage(request):
    return render(request, 'detailspage.html')

def createpropertypage(request):
    return render(request, 'createproperty.html')

def mapview(request):
    return render(request, 'mapview.html')

def listview(request):
    myproperty = Property.objects.all()
    template = loader.get_template('listpage.html')
    context = {
        'mypropertys' : myproperty,
<<<<<<< HEAD
        'sort_choices': sort_choices,
=======
>>>>>>> f2a365cbb09c998935db0e3912ac379dc99ead4c
        'bathroom_choices': bathroom_choices,
        'bedroom_choices': bedroom_choices,
        'parking_choices': parking_choices,
        'price_choices': price_choices
    }
    return HttpResponse(template.render(context, request))

class PropertyDetailView(View):
    def get(self, request, *args, **kwargs):
        property = get_object_or_404(Property, id=kwargs['id'])
        context = {'property': property}
        print(property.image)
        return render(request, 'detailspage.html', context)

@csrf_protect
def storeProperty(request):
    prop = Property()
    prop.image = request.POST.get('prop_image')
    prop.title = request.POST.get('prop_title')
    prop.address = request.POST.get('prop_address')
    prop.suburb = request.POST.get('prop_suburb')
    prop.state = request.POST.get('prop_state')
    prop.postcode = request.POST.get('prop_pcode')
    prop.price = request.POST.get('prop_price')
    prop.bedroom = request.POST.get('prop_bedroom')
    prop.bathroom = request.POST.get('prop_bedroom')
    prop.parking_space = request.POST.get('prop_parking')
    prop.description = request.POST.get('prop_description')
    prop.landlord = request.user
    prop.save()
    messages.success(request, "Property Added Successfully")
    return redirect('/listpage')

class PropertyEditView(View):
    def get(self, request, *args, **kwargs):
        property = get_object_or_404(Property, id=kwargs['id'])
        context = {'property': property}
        return render(request, 'editproperty.html', context)

@csrf_protect
def updateProperty(request, *args, **kwargs):
    prop = get_object_or_404(Property, id = kwargs['id'])
    prop.image = request.POST.get('prop_image')
    prop.title = request.POST.get('prop_title')
    prop.address = request.POST.get('prop_address')
    prop.suburb = request.POST.get('prop_suburb')
    prop.state = request.POST.get('prop_state')
    prop.postcode = request.POST.get('prop_pcode')
    prop.price = request.POST.get('prop_price')
    prop.bedroom = request.POST.get('prop_bedroom')
    prop.bathroom = request.POST.get('prop_bathroom')
    prop.parking_space = request.POST.get('prop_parking')
    prop.description = request.POST.get('prop_description')
    prop.landlord = request.user
    prop.save()
    messages.success(request, "Property Update Successfully")
    return redirect('/listpage/')

def deleteProperty(request, *args, **kwargs):
    prop = get_object_or_404(Property, id = kwargs['id'])
    prop.delete()
    return redirect('/listpage/')
    
def searchProperty(request):
    queryset_list = Property.objects.order_by('id')

  # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(address__icontains=keywords) | Q(suburb__icontains=keywords) | 
                                                Q(state__icontains=keywords) | Q(postcode__icontains=keywords))
    if 'bedroom' in request.GET:
        bedrooms = request.GET['bedroom']
        if bedrooms:
            queryset_list = queryset_list.filter(bedroom__lte=bedrooms)

    if 'bathroom' in request.GET:
        bathrooms = request.GET['bathroom']
        if bathrooms:
            queryset_list = queryset_list.filter(bathroom__lte=bathrooms)

    if 'parking' in request.GET:
        parking = request.GET['parking']
        if parking:
            queryset_list = queryset_list.filter(parking_space__lte=parking)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'sort_choices': sort_choices,
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'parking_choices': parking_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'searchproperty.html', context)

def sortProperty(request):
    queryset_list_order = Property.objects.order_by('id')

    if 'latest' in request.GET:
        queryset_list_order = Property.objects.order_by('price').all()

    if 'priceAsc' in request.GET:
        queryset_list_order = Property.objects.order_by('-price').all()

    if 'priceDesc' in request.GET:
        queryset_list_order = Property.objects.order_by(Property.price.desc()).all()

    context = {
        'sort_choices': sort_choices,
        'listings': queryset_list_order,
        'values': request.GET
    }

    return render(request, 'searchproperty.html', context)      