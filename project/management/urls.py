from django.urls import path, include
from rest_framework import urls
from .views import *

lecture_list = LectureViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

lecture_detail = LectureViewSet.as_view({
    'get': 'retrieve',
    'put': 'update'
    'delete': 'delete'
})

chapter = ChapterViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

chapter_detail = ChapterViewSet.as_view({
    'get': 'retrieve',
    'put': 'update'
    'delete': 'delete'
})

urlpatterns = [
    path('lecture/', lecture_list),
    path('lecture/<int:pk>/', lecture_detail),
    path('chapter/', chapter),
    path('chapter/<int:pk>/', chapter_detail),
	]
