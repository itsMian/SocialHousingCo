from django.shortcuts import render, redirect, get_object_or_404
from Database.models import Property
from django.http import HttpResponse
from django.template import loader
from django.views import View
from Listpage.choices import bedroom_choices, bathroom_choices, parking_choices, price_choices
from django.views.decorators.csrf import csrf_protect




# def home(request):
#     if 'keywords' in request.GET:
#         keywords = request.GET['keywords']
#         if keywords:
#             queryset_list = queryset_list.filter(Q(address__icontains=keywords) | Q(suburb__icontains=keywords) | 
#                                                 Q(state__icontains=keywords) | Q(postcode__icontains=keywords))
#     if 'bedroom' in request.GET:
#         bedrooms = request.GET['bedroom']
#         if bedrooms:
#             queryset_list = queryset_list.filter(bedroom__lte=bedrooms)

#     if 'bathroom' in request.GET:
#         bathrooms = request.GET['bathroom']
#         if bathrooms:
#             queryset_list = queryset_list.filter(bathroom__lte=bathrooms)

#     if 'parking' in request.GET:
#         parking = request.GET['parking']
#         if parking:
#             queryset_list = queryset_list.filter(parking_space__lte=parking)

#     if 'price' in request.GET:
#         price = request.GET['price']
#         if price:
#             queryset_list = queryset_list.filter(price__lte=price)
#     context = {
#         'bedroom_choices': bedroom_choices,
#         'bathroom_choices': bathroom_choices,
#         'parking_choices': parking_choices,
#         'price_choices': price_choices,
#         'listings': queryset_list,
#         'values': request.GET
#     }
#     return render(request, 'homepage.html', context)

def home(request):
    myproperty = Property.objects.all()
    template = loader.get_template('homepage.html')
    context = {
        'mypropertys' : myproperty,
        'bathroom_choices': bathroom_choices,
        'bedroom_choices': bedroom_choices,
        'parking_choices': parking_choices,
        'price_choices': price_choices
    }
    return HttpResponse(template.render(context, request))