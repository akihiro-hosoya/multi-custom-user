from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

# Create your models here.
class User(models.Model):
    account = models.OneToOneField(CustomUser, verbose_name='アカウント', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(('作成日'), default=timezone.now)