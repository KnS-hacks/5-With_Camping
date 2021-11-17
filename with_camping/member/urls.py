from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='member_login'),
    path('signup/', views.sign_up, name='sign_up'),
    path('logout/', views.logout, name='member_logout'),
]