from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Vehicle, CarChoice
from .forms import RegisterForm

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

def register(request):

        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            first_name =form.cleaned_data['first_name']
            last_name =form.cleaned_data['last_name']
            email =form.cleaned_data['email']
            account_type = form.cleaned_data['account_type']

            print(first_name, last_name, email, account_type)
            if account_type == 'DRIVER':
                return HttpResponseRedirect('/myJourneys/register/driver')

            return HttpResponseRedirect('/myJourneys/register/successful')
        else:
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def register_driver(request):
    context = {}

    return render(request, 'register-driver.html', context=context)

def register_success(request):
    context = {}

    return render(request, 'registration-successful.html', context=context)



def index_redirect(request):
    return HttpResponsePermanentRedirect('/myJourneys/')