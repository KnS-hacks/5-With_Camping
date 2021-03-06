from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from member.models import Member
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.
# 캠핑용품 목록
def camping_tool(request):
    camping_tools = CampingTools.objects.all()
    # camping_tools = get_object_or_404(CampingTools, pk = id)
    return render (request, 'camping_tools.html', {'camping_tools':camping_tools})

# 특정 캠핑용품의 세부사항
def camping_tool_detail(request, id):
    camping_tools = get_object_or_404(CampingTools, id = id)
    user_id = request.user.id
    
    return render(request, 'camping_tools_detail.html', {'camping_tools':camping_tools, 'user':user_id})

# 특정 캠핑용품 대여
def rent_camping_tool(request):
    return HttpResponse('Rent a camping tool')

#############################################################

# 특정 캠핑용품 구매
def purchase_camping_tool(request, id, user_id):
    camping_tools = get_object_or_404(CampingTools, pk = id)
    new_order = OrderList()
    user = Member.objects.get(id = user_id)
    new_order.order_Member = user
    new_order.order_List = camping_tools
    new_order.save() 
    return render(request, 'order_finish.html', {'new_order':new_order})

# 캠핑용품 주문 내역 (결제 창)
def order_list(request, user_id) : 
    o_list = OrderList.objects.all()
    p_list = CampingTools.objects.all()

    o_list = o_list.filter(order_Member = user_id)

    result = []
    total = 0
    for i in o_list : 
        for j in p_list : 
            if str(i) == str(j) : 
                total += int(j.productPrice) 
                result.append(j)
                
    return render(request, 'order_lists.html', {'result':result, 'total':total})