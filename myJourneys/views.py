from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from .models import Vehicle, CarChoice

# Create your views here.
def index(request):

    v = Vehicle(vehicle_id = 1, type= CarChoice.TUK, capacity= 3, license_plate_number= "hjdhwhgdhjw")
    vehicle_type = v.type.name
    vehicle_id = v.vehicle_id

    context = {
        'vehicle_type': vehicle_type,
         'vehicle_id': vehicle_id,
    }
    return render(request, 'index.html', context=context)

def dashboard(request):

    # v = Vehicle(vehicle_id = 1, type= CarChoice.TUK, capacity= 3, license_plate_number= "hjdhwhgdhjw")
    # vehicle_type = v.type.name
    # vehicle_id = v.vehicle_id

    context = {
        # 'vehicle_type': vehicle_type,
        #  'vehicle_id': vehicle_id,
    }
    return render(request, 'dashboard.html', context=context)

def account(request):
    context = {}

    return render(request, 'account.html', context=context)

def register(request):
    context = {}

    return render(request, 'register.html', context=context)

def booking(request):
    context = {}

    return render(request, 'booking.html', context=context)

def index_redirect(request):
    return HttpResponsePermanentRedirect('/myJourneys/')