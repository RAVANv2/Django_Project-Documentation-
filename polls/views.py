from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Include Function
def index(request):
    return HttpResponse("Hello world this is python polls django views")
