from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.
def home (request) :
    return render(request, 'home.html')


