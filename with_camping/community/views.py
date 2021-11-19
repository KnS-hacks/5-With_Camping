from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BulletinPostForm
from .models import *
from member.models import Member

# Create your views here.
# 캠핑 커뮤니티 게시판
def camping_community(request):
    bulletin_posts = BulletinPost.objects.all()
    return render (request, 'community.html', {'bulletin_posts':bulletin_posts})

# 캠핑장 게시판
def camping_ground(request):
    return HttpResponse("Bulletin board of camping ground")

# 자유게시판
def free(request):
    return HttpResponse("Bulletin board of free topic")

def write(request):
    if request.method == 'POST': # method가 post일때
        new_write = BulletinPost()
        new_write.title = request.POST['title']
        new_write.image = request.FILES.get('image')
        new_write.body = request.POST['body']
        user_id = request.user.id
        user = Member.objects.get(id = user_id)
        new_write.author = user
        new_write.save()
        return redirect('home')
    else:
        return render(request, 'write.html')
