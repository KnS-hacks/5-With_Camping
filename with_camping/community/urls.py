from django.urls import path

from . import views

urlpatterns = [
    path('', views.camping_community, name="camping_community"),
    path('free/', views.free, name="free_bulletin"),
    path('create/', views.create, name="create"),
]