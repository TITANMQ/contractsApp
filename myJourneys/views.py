from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate
from django.urls import reverse
from django.db.models import Q
from .models import Customer, Driver, Vehicle, CarChoice, User, Bookings, StatusChoice
from .forms import DriverRegisterForm, RegisterForm, LoginForm, BookingForm, AccountForm
import random


# code for handling index(home) requests
def index(request):
    context = {

    }


    return render(request, 'index.html', context=context)

# code for handling the user dashboard requests
def dashboard_user(request):

    cust =  Customer.objects.get(user_id=request.session['user_id'])
    bookings_list = Bookings.objects.all().filter(customer=cust, status=StatusChoice.ON_GOING.value)

    print(cust.last_name)
    
    for booking in bookings_list:
        if booking.assigned_driver == None:
            print('Driver not assigned yet')
        print(booking.booking_id)
    past_bookings_list = Bookings.objects.all().filter(Q(customer=cust), Q(status=StatusChoice.CANCELLED.value) | Q(status =StatusChoice.COMPLETED.value))

    
    context = {
        'booking_list': bookings_list,
        'past_booking_list': past_bookings_list,
        'no_driver': _('Driver not assigned yet')
    }
    return render(request, 'dashboard_user.html', context=context)

# code for handling canceling booking requests
def cancel_booking(request):
    return

# code for handling accepting booking requests
def accept_booking(request, booking_id, driver_id):
    
    booking = Bookings.objects.get(booking_id=booking_id)

    print('called')
    print(booking.assigned_driver)
    if booking.assigned_driver == None:
        driver = Driver.objects.get(user_id =driver_id)
        booking.assigned_driver = driver
        booking.save()


    return HttpResponseRedirect(reverse('dashboard_driver'))

# code for handling the driver dashboard requests
# gets drivers current bookings, past bookings and all available bookings that can be 
#accepted
def dashboard_driver(request):

    print('called')
    driver =  Driver.objects.get(user_id=request.session['user_id'])
    print(driver.user_id)
    available_bookings_list = Bookings.objects.all().filter(assigned_driver=None, status=StatusChoice.ON_GOING.value)

    for booking in available_bookings_list:
        print(booking.booking_id)
            
    past_bookings_list = Bookings.objects.all().filter(assigned_driver=driver, status=StatusChoice.COMPLETED.value)

            
    current_bookings_list = Bookings.objects.all().filter(assigned_driver=driver, status=StatusChoice.ON_GOING.value)       


    context = {
        # 'form': form,
        'available_bookings_list': available_bookings_list,
        'past_bookings_list': past_bookings_list,
        'current_bookings_list': current_bookings_list,
        'current_bookings_list_length': len(current_bookings_list),
        'past_bookings_list_length': len(past_bookings_list),
        'available_bookings_list_length': len(available_bookings_list),
        'driver':driver
        
    }
    return render(request, 'dashboard_driver.html', context=context)

# code for handling the account requests which gets account infomation and 
# allows users to update any details of their account
def account(request):

    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']


            customer = Customer.objects.get(user_id=request.session['user_id'])

            if password == confirm_password:

                customer.first_name = first_name
                customer.last_name = last_name
                customer.email_address = email
                customer.phone_number = phone
                customer.password = password

                customer.save()
                
        else:
            print(form.errors)
    else:
        customer = Customer.objects.get(user_id=request.session['user_id'])
        form = AccountForm(initial={"first_name":customer.first_name, 
        "last_name": customer.last_name, "email": customer.email_address, 
        "phone": customer.phone_number })
        

    return render(request, 'account.html', {'form': form})

# code for handling the bookings requests which allows customers to create new bookings
def bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            pick_up = form.cleaned_data['pick_up']
            drop_off = form.cleaned_data['drop_off']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            notes = form.cleaned_data['notes']
            customer = Customer.objects.get(user_id=request.session['user_id']) 
            status = StatusChoice.ON_GOING.value


            book = Bookings(pick_up=pick_up, drop_off=drop_off, date=date, time=time, customer=customer, notes=notes, status=status)
            book.save()

        else:
            print(form.errors)
    else:
        form = BookingForm()

    return render(request, 'bookings.html', {'form': form})

# code for handling the register requests where users can sign up as either a driver
# or a customer
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

                    driver = Driver(username=username, first_name=first_name, last_name=last_name, email_address=email,
                                    password=password)
                    vehicle = Vehicle()
                    vehicle.license_plate_number = random.randrange(100000)
                    vehicle.save()
                    driver.vehicle = vehicle
                    driver.save()
                    request.session['user_id'] = driver.user_id

                    return HttpResponseRedirect('register/driver')
                else:
                    cust = Customer(username=username, first_name=first_name, last_name=last_name, email_address=email,
                                    password=password)
                    cust.save()
                    request.session['user_id'] = cust.user_id

                    if Customer.objects.get(user_id=cust.user_id).username == cust.username:
                        print(Customer.objects.get(user_id=cust.user_id).username)
                    else:

                        print('database error')
                    print(request.LANGUAGE_CODE)
                    return HttpResponsePermanentRedirect('register/successful')

                return
        else:
            # print(form.errors)
            print(form['confirm_password'].errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

# code for handling the driver register requests which is an additional step to 
# driver register which allows new drivers to add there vehicle 
def register_driver(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DriverRegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            vehicle_type = form.cleaned_data['vehicle_type']
            capacity = form.cleaned_data['capacity']
            license_plate = form.cleaned_data['license_plate']

            user_id = request.session['user_id']

            driver = Driver.objects.get(user_id=user_id)
            print(driver.username)

            vehicle = driver.vehicle
            vehicle.type = vehicle_type
            vehicle.capacity = capacity
            vehicle.license_plate_number = license_plate

            vehicle.save()

            
            return HttpResponseRedirect('successful')
            
    
    else:
        form = DriverRegisterForm()

    return render(request, 'register_driver.html', {'form': form})

# code for handling register success requests which is a confirmation page when a 
# users successfully creates a new account
def register_success(request):
    account_type = request.session['account_type']  # Get the account type

    context = {'account_type': account_type}

    return render(request, 'registration_successful.html', context=context)


# code for handling index redirect requests which redirects users from the root url
# to the home page (index)
def index_redirect(request):
    return HttpResponsePermanentRedirect('myJourneys/')

# code for handling login requests which allows uses to login to their
# accounts with a username and passord
def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            usr = User.objects.get(username=username)

            if usr.password == password:

                if Customer.objects.filter(user_id=usr.user_id).count() > 0:
                    request.session['user_id'] = usr.user_id
                    request.session.set_expiry(7200) # sets session expiry for 2 hours 

                    return HttpResponsePermanentRedirect('user/dashboard')

                else:
                    request.session['user_id'] = usr.user_id
                    request.session.set_expiry(7200) # sets session expiry for 2 hours 

                    return HttpResponsePermanentRedirect('driver/dashboard')

                return
        else:
            print(form.errors)

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout(request):
    
    print('logout')
    request.session.flush()


    return HttpResponseRedirect(reverse('login'))

# support function for translating strings
def translate(language, msg):
    current_language = get_language()
    try:
        activate(language)
        text = _(msg)
    finally:
        activate(current_language)
