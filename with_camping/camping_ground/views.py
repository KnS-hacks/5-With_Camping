from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 캠핑장 목록
def camping_ground_list(request):
    return HttpResponse('This is list of camping ground')

# 특정 캠핑장의 세부사항
def camping_ground_detail(request):
    return HttpResponse('Details of specific camping ground')

# 특정 캠핑장 예약
def register_camping_ground(request):
    return HttpResponse('Register a camping ground')