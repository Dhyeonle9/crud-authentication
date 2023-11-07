from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()

    # 유저 모델을 참조하는 경우
    # 1. 권장 x
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    # 2. 권장 -> settings.AUTH_USER_MODEL == 'accounts.User' 유지보수에 유리
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 3. 권장 -> auth에서 get_user_model 함수를 가져와 실행결과를 ForeignKey에 참조값으로 씀
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)