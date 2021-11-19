from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Member
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# 로그인(default)
def member_login(request) :
     if request.method == "POST" : 
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        print(username)
        print(password)
        if user is not None : 
            login(request, user)
            print("성공")
            return redirect('home')
        else : 
            print("실패")
            return render(request, 'login.html', {'error' : '아이디와 비밀번호가 맞지 않습니다. '})
     else : 
        return render(request, 'login.html')

# 로그아웃 (default)
def member_logout(request) :
    logout(request)
    return redirect('home')

# 회원가입
def sign_up(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = Member.objects.create_user(
                username = request.POST["username"],
                people_name = request.POST["people_name"],
                password = request.POST["password"], 
                nickname = request.POST["nickname"],
            ) 
            user.save()
            auth.login(request, user)
            return redirect('home')
        else : 
            return render(request, 'signup.html')
    else: 
        return render(request, 'signup.html')