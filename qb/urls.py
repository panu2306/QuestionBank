from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    #path('',views.index, name='index'),
    path('', views.index, name='try_form'),
    #path('ack', views.acknowledge, name='ack-page'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)