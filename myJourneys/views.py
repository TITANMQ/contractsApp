from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import RegisterForm


# Create your views here.
def index(request):
    context = {

    }
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
            email = form.cleaned_data['email']
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

    return render(request, 'register_driver.html', context=context)


def register_success(request):
    context = {}

    return render(request, 'registration_successful.html', context=context)


def index_redirect(request):
    return HttpResponsePermanentRedirect('/myJourneys/')
