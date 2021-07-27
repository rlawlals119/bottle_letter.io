from django.shortcuts import render,redirect
from .models import Letter
# Create your views here.

def home(request):
    return render(request,'home.html')

def write(request):
    return render(request,'write.html')

def create(request):
    new_letter = Letter()
    new_letter.body = request.POST['body']
    new_letter.save()
    return render(request,'create.html')

def read(request):
    return render(request, 'read.html')