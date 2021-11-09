from django.urls import path

from . import views

urlpatterns = [
    path('', views.camping_ground_list, name = 'camping_ground_list'),
    path('detail/', views.camping_ground_detail, name = 'camping_ground_detail'),
    path('register/', views.register_camping_ground, name = 'regiser_camping_ground'),

]