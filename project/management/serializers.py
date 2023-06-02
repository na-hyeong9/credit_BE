from rest_framework import serializers
from .models import *

class LectureSerializer(serializers.ModelSerializer) :
    class Meta :
        model = lecture        # management 모델 사용
        fields = '__all__'            # 모든 필드 포함

class ChapterSerializer(serializers.ModelSerializer) :
    class Meta :
        model = chapter        # chapter 모델 사용
        fields = '__all__'            # 모든 필드 포함