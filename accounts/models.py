from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass
    # article_set 장고가 자동으로 생성해주는 컬럼(ForeignKey)
    # comment_set 장고가 자동으로 생성해주는 컬럼(Foreignkey)