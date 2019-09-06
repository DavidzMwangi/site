from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bases', views.base, name='bases'),
    path('login', views.login, name='bases'),
]