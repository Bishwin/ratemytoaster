from django.urls import path
from .views import BirdAddView, BirdListView

urlpatterns = [
    path('add', BirdAddView.as_view(), name="bird_add"),
    path('', BirdListView.as_view(), name="bird_list")
]