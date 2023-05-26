from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from Database.models import Property
from django.http import Http404
from django.views import View
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

def index(request):
    return render(request, 'listpage.html')

def detailspage(request):
    return render(request, 'detailspage.html')

def createpropertypage(request):
    return render(request, 'createproperty.html')

def listview(request):
    myproperty = Property.objects.all()
    template = loader.get_template('listpage.html')
    context = {
        'mypropertys' : myproperty
    }
    return HttpResponse(template.render(context, request))

class PropertyDetailView(View):
    def get(self, request, *args, **kwargs):
        property = get_object_or_404(Property, id=kwargs['id'])
        context = {'property': property}
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
    prop.save()
    messages.success(request, "Property Update Successfully")
    return redirect('/listpage/')

def deleteProperty(request, *args, **kwargs):
    prop = get_object_or_404(Property, id = kwargs['id'])
    prop.delete()
    return redirect('/listpage/')

def searchProperty(request):
    query_list = Property.objects.order_by('-id')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(address_icontains=keywords)
