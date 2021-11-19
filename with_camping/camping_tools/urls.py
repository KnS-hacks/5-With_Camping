from django.urls import path
from . import views

urlpatterns = [
    path('', views.camping_tool, name = 'camping_tool'),
    path('<int:id>', views.camping_tool_detail, name = 'camping_tool_detail'),
    path('rent/', views.rent_camping_tool, name = 'rent_camping_tool'),
    path('purchase/<int:id>/<int:user_id>', views.purchase_camping_tool, name='purchase_camping_tool'),
] 