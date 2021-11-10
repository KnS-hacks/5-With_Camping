from django.urls import path

from . import views

urlpatterns = [
    path("", views.camping_tools, name="camping_tools_bulletin"),
    path("campingGround/", views.camping_ground, name="camping_ground_bulletin"),
    path("free/", views.free, name="free_bulletin"),
    path("create/", views.create, name="create"),

]