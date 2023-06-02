from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets

from .models import *
from .serializers import *

# Create your views here.
class LectureViewSet(viewsets.ModelViewSet):
    def get(self, request):
        Lecture = lecture.objects.all()
        #print(Lecture)
        LectureSerializer = LectureSerializer(Lecture, many=True)
        return Response(LectureSerializer.data, LectureSerializer.data)

class ChapterViewSet(viewsets.ModelViewSet):
    def get(self, request):
        Chapter = chapter.objects.all()
        #print(Lecture)
        ChapterSerializer = ChapterSerializer(Chapter, many=True)
        return Response(LectureSerializer.data)