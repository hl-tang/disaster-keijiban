from django.db import models
from account.models import User

# Create your models here.
class Disaster(models.Model):
    disaster_name = models.CharField(max_length=200)
    allow_areas = models.JSONField()

class Post(models.Model):
    # post_id = models.CharField(max_length=100, primary_key=True)
    # disaster = models.ForeignKey(Disaster, on_delete=models.CASCADE) # 得到对应的allow_areas
    disaster_id = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    user_name = models.CharField(max_length=200)
    last_date = models.DateTimeField(auto_now=True)
    tag_id = models.IntegerField(default=0) # 1:行方不明 2:2次避難 3:物資不足 4:ボランティア募集
    # images = models.ImageField(upload_to='media/', null=True, blank=True) # 先传1张
    images = models.CharField(max_length=200, null=True, blank=True)
