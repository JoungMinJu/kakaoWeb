from django.db import models

# Create your models here.
class Recommend_history(models.Model):
    # 아이디
    id = models.AutoField(primary_key = True)
    # 추천
    recommend = models.CharField(max_length = 1000)
    # 생성일자
    created_at = models.DateTimeField(auto_now= True)