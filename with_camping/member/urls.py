from django.urls import path

from . import views

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('signUp/', views.sign_up, name='sign_up'),
]