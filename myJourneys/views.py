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
    # return HttpResponse("Bruh")

def index_redirect(request):
    return HttpResponsePermanentRedirect('/myJourneys/')