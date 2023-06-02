from django.db import models
from django.core.validators import FileCountValidator, ValidationError # 개수 제한/ 유효성 검사

# Create your models here.
class lecture(models.Model):
    title = models.CharField(max_length=50)
    chapter = models.ManyToManyField("chapter")

class chapter(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(
        upload_to='videos/',
        validators=[FileCountValidator(max_count=1)])# 최대 1개

    def __str__(self):
        return self.title
    
    # 유효성 검사
    def clean(self):
        super().clean() # 부모 클래스
        if self.video_file:
            allowed_formats = ['mp4', 'avi', 'mkv']  # 허용되는 파일 형식 리스트
            file_extension = self.video_file.name.split('.')[-1] # '.' 으로 구분하여 리스트로 저장하여 확장자명을 추출
            if file_extension not in allowed_formats:
                raise ValidationError("비디오 파일 형식이 잘못되었습니다.") # 에러 메세지 반환
    
    def save(self, *args, **kwargs):
        try:
            self.full_clean()
        except ValidationError:
            # Do something when validation is not passing
            pass
        else:
            # Validation is ok we will save the instance
            super().save(*args, **kwargs)