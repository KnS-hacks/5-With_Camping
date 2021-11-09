from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 캠핑용품 게시판
def camping_tools(request):
    return HttpResponse("Bulletin board of camping tools")

# 캠핑장 게시판
def camping_ground(request):
    return HttpResponse("Bulletin board of camping ground")

# 자유게시판
def free(request):
    return HttpResponse("Bulletin board of free topic")