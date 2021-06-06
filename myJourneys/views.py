from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("App under contruction")

def index_redirect(request):
    return HttpResponsePermanentRedirect('/myJourneys/')