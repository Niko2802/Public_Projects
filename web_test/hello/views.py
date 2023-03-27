from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request, name):
    return HttpResponse(f"Hello django {name}")

def about(request):
    print(request.body)
    print(request.method)
    print(request.GET)
    print(request.COOKIES)
    return HttpResponse("Info about me")

def blogs(request, year):
    return HttpResponse(f"<h2>blog {year}</h2>")

def test(request):
    return HttpResponseRedirect("about")
