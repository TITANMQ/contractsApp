from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Customer, Driver, Vehicle, CarChoice, User
from .forms import DriverRegisterForm, RegisterForm


# Create your views here.
def index(request):
    context = {

    }


    driver = Driver.objects.get(user_id= 2)

    print(driver.username)
    print(driver.vehicle.type)
    print(driver.vehicle.capacity)
    print(driver.vehicle.license_plate_number)

    # vehicle = Vehicle.objects.get(vehicle_id= 1)
    # vehicle.delete()

    return render(request, 'index.html', context=context)


def dashboard_user(request):
    context = {

    }
    return render(request, 'dashboard_user.html', context=context)


def dashboard_driver(request):
    context = {

    }
    return render(request, 'dashboard_driver.html', context=context)


def account(request):
    context = {}

    return render(request, 'account.html', context=context)


def bookings(request):
    context = {}

    return render(request, 'bookings.html', context=context)


def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            account_type = form.cleaned_data['account_type']

            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                # print(first_name, last_name, email, account_type)

                request.session['account_type'] = account_type.lower()
                
                if account_type == 'DRIVER':

                    driver = Driver(username=username,  first_name = first_name, last_name=last_name, email_address=email, password=password)
                    vehicle = Vehicle()
                    vehicle.save()
                    driver.vehicle = vehicle
                    driver.save()
                    request.session['user_id'] = driver.user_id 
                    return HttpResponseRedirect('/myJourneys/register/driver')
                else:
                    cust = Customer(username=username,  first_name = first_name, last_name=last_name, email_address=email, password=password)
                    cust.save()
                    request.session['user_id'] = cust.user_id 

                    if Customer.objects.get(user_id=cust.user_id).username == cust.username:
                        print(Customer.objects.get(user_id=cust.user_id).username)
                    else:

                        print('database error')
    
                    return HttpResponsePermanentRedirect('/myJourneys/register/successful')

                return
        else:
            print(form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def register_driver(request):
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DriverRegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            vehicle_type = form.cleaned_data['vehicle_type']
            capacity= form.cleaned_data['capacity']
            license_plate = form.cleaned_data['license_plate']

        
            user_id = request.session['user_id'] 

            driver = Driver.objects.get(user_id=user_id)
            print(driver.username)

            vehicle = driver.vehicle
            vehicle.type = vehicle_type
            vehicle.capacity = capacity
            vehicle.license_plate_number = license_plate

            vehicle.save()
            
            return HttpResponseRedirect('/myJourneys/register/successful')
            
    
    else:
        form = DriverRegisterForm()

    return render(request, 'register_driver.html', {'form': form})


def register_success(request):

    account_type = request.session['account_type'] # Get the account type

    context = {'account_type': account_type }

    return render(request, 'registration_successful.html', context=context)


def index_redirect(request):
    return HttpResponsePermanentRedirect('/myJourneys/')
