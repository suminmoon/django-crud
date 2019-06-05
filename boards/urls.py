from django.urls import path
from . import views
urlpatterns = [

    path('', views.index),   # '' -> boars/ 경로
    path('new/', views.new),  # 사용자 입력 페이지
    path('create/', views.create),  # data 저장하는 페이지
]