from django.urls import path
from . import views

urlpatterns = [
    path('', views.camping_tool, name = 'camping_tool'),
    path('<str:id>', views.camping_tool_detail, name = 'camping_tool_detail'),
    path('rent/', views.rent_camping_tool, name = 'rent_camping_tool'),
    path('purchase/<str:id>/<str:user_id>', views.purchase_camping_tool, name='purchase_camping_tool'),
] 