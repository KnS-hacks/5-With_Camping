from django.urls import path

from . import views

urlpatterns = [
    path('', views.camping_tools_list, name = 'camping_tools_list'),
    path('detail/', views.camping_tool_detail, name = 'camping_tool_detail'),
    path('rent/', views.rent_camping_tool, name = 'rent_camping_tool'),
    path('purchase/', views.purchase_camping_tool, name = 'purchase_camping_tool'),

]