from django.urls import path

from . import views

urlpatterns = [
    path('', views.albums_list, name='albums_list'),
]