from django.shortcuts import render
from django.http import HttpResponse
#home page (index)
def index(request):
    return HttpResponse(r"<a href='/rango/about/'>About</a>"+'Rango says hey there partner!')
#about page(about)
def about(request):
    return HttpResponse(r"<a href='/rango/'>Index</a>"+'Rango says here is the about page.')
# Create your views here.
