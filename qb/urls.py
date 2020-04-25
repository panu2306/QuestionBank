from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('register/', views.register, name='register'),
    path('qb/', views.QuestionListView.as_view(), name='question_list'),
    path('qb/<int:id>', views.question_detail, name='question_detail'),
    #path('qb/<int:id>', views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)