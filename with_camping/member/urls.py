from django.urls import path

from .import views

urlpatterns = [
    path('', views.member_login, name='member_login'),
    path('signup/', views.sign_up, name='sign_up'),
    path('logout/', views.member_logout, name='member_logout'),
]