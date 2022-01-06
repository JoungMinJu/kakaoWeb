from django.db import models

# Create your models here.
class Recommend_history(models.Model):
    id = models.AutoField(primary_key = True)
    recommend = models.CharField(max_length = 1000)
    created_at = models.DateTimeField(auto_now= True)