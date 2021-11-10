from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BulletinPost
from .forms import BulletinPostForm

# Create your views here.
# 캠핑용품 게시판
def camping_tools(request):
    bulletin_post = BulletinPost.objects
    return render(request, "community.html", {"bulletin_post" : bulletin_post})

# 캠핑장 게시판
def camping_ground(request):
    return HttpResponse("Bulletin board of camping ground")

# 자유게시판
def free(request):
    return HttpResponse("Bulletin board of free topic")

def create(request):
    if request.method == 'POST': # method가 post일때
        form = BulletinPostForm(request.POST) # form 에 ReviewForm 할당

        if form.is_valid(): # form 유효성 검증
            form.save() # 저장
            return redirect('community.html') # 다시 main으로
    else:
        form = BulletinPostForm() # 빈 form 열기

    return render(request, 'create.html',{'form' :form})