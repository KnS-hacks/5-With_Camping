from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

# 로그인(default)
def sign_in(request):
    return HttpResponse('Sign in to use our service')

# 회원가입
def sign_up(request):
    return HttpResponse('Sign up to use our service')