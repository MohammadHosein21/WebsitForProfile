from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblog, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
