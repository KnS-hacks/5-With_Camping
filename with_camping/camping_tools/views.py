from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 캠핑용품 목록
def camping_tools_list(request):
    return HttpResponse('This is list of camping tools')

# 특정 캠핑용품의 세부사항
def camping_tool_detail(request):
    return HttpResponse('Details of specific camping tool')

# 특정 캠핑용품 대여
def rent_camping_tool(request):
    return HttpResponse('Rent a camping tool')

# 특정 캠핑용품 구매
def purchase_camping_tool(request):
    return HttpResponse('Purchase a camping tool')