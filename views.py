from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def WELCOME(request):
    return render(request, 'DEMOAPP1/WELCOME.html')
