from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('up', views.upload, name='upload'),
]