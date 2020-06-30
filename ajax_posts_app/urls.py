from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_post_ajax', views.create_post_ajax)
]
