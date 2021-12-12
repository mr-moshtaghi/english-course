from django.db import models


# Create your models here.
from core import const


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Course(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/course/', null=True, blank=True)

    def __str__(self):
        return self.title

    def is_viewed(self, user):
        return self.course_user.filter(user=user).exists()


class Video(BaseModel):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='images/videos/', null=True, blank=True)
    course = models.ForeignKey(Course, related_name='video', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def is_viewed(self, user):
        return self.video_user.filter(user=user).exists()


class Word(BaseModel):
    english_word = models.CharField(max_length=255)
    translate = models.CharField(max_length=255)
    video = models.ForeignKey(Video, related_name='words', on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=20,
                            choices=const.WORD_TYPES,
                            default=const.WORD_TYPE_ONE)

    def __str__(self):
        return f"{self.english_word}={self.translate}"

    def is_viewed(self, user):
        return self.word_user.filter(user=user).exists()

    def is_learned(self, user):
        return self.word_user.filter(user=user, status='learned').exists()

class CourseUser(BaseModel):
    user = models.ForeignKey('account.CustomUser', related_name='course_user', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='course_user', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'course']

    def __str__(self):
        return f"{self.user}={self.course}"


class VideoUser(BaseModel):
    user = models.ForeignKey('account.CustomUser', related_name='video_user', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name='video_user', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'video']

    def __str__(self):
        return f"{self.user}={self.video}"


class WordUser(BaseModel):
    user = models.ForeignKey('account.CustomUser', related_name='word_user', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='word_user', on_delete=models.CASCADE)
    status = models.CharField(max_length=20,
                              choices=const.WORD_USER_STATUS_CHOICES,
                              default=const.WORD_USER_STATUS_NOT_LEARNED)

    class Meta:
        unique_together = ['user', 'word']

    def __str__(self):
        return f"{self.user}={self.word}"
