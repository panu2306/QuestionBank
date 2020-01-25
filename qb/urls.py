from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('try_form', views.try_form, name='try_form'),
    path('ack', views.acknowledge, name='ack-page')
]
