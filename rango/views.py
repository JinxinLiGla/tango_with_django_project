from django.shortcuts import render
from django.http import HttpResponse
#home page (index)
def index(request):
    context_dict = {'boldmessage':'Crunchy, creamy, cookie, candy, cupcake!'}
    #return HttpResponse(r"<a href='/rango/about/'>About</a>"+'Rango says hey there partner!')
    return render(request, 'rango/index.html', context=context_dict)
#about page(about)
def about(request):
    #return HttpResponse(r"<a href='/rango/'>Index</a>"+'Rango says here is the about page.')
    context_dict = {'boldmessage': 'This tutorial has been put together by Jinxin'}
    return render(request, 'rango/about.html', context=context_dict)
# Create your views here.
