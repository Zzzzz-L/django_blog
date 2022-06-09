from django.db import models
from django.contrib.auth.models import User
# timezone
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    # 创建者
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 文章标题
    title = models.CharField(max_length=100)
    # 文章正文
    content = models.TextField()
    # 文章创建时间
    created_at = models.DateTimeField(default=timezone.now,)
    # 文章更新时间
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # 按照时间降序排列
        ordering = ['-created_at']

    def __str__(self):
        return self.title