from __future__ import unicode_literals  # 문자 인코딩
from django.utils import timezone
from django.db import models


# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)  # 등록 시점
    body = models.TextField(default='')
    mood = models.CharField(max_length=200, default='')
