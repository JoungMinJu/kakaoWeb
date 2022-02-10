from django.db import models
import sys
sys.path.append('..')
from user.models import User
# Create your models here.


class Community(models.Model):
    CATEGORY = (
        ('후기','후기'),
        ('사담','사담'),
        ('질문','질문'),
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='community/', blank=True, null=True)
    view_count  = models.PositiveIntegerField(default=0)
    like_user_set = models.ManyToManyField(User, blank=True, related_name='like_user_set', through ='Like')
    category = models.CharField(max_length = 1000, choices=CATEGORY)

    def __str__(self):
        return self.title
    def summar(self):
        return self.body[:20]
    @property
    def like_count(self):
        return self.like_user_set.count()

class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='like')
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        unique_together = (('user','community'))