from django.shortcuts import render, redirect
from django.http import HttpResponse

from camping_ground.models import CampingGround

# Create your views here.
# 캠핑장 목록
def camping_ground_list(request):
    return HttpResponse('Camping ground list')

# 특정 캠핑장의 세부사항
def camping_ground_detail(request):
    return HttpResponse('Details of specific camping ground')

# 특정 캠핑장 예약
def register_camping_ground(request):
    return HttpResponse('Register a camping ground')