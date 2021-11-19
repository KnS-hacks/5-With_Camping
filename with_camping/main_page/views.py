from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from camping_ground.models import CampingGround
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.
def home (request) :
    campgrounds = CampingGround.objects.all()
    context = {"campgrounds":campgrounds}
    return render(request, "home.html", context)

# 특정 캠핑장의 세부사항
def detail(request):
    return render(request, "reservation_detail.html")