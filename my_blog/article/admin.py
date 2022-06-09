from django.contrib import admin

# Register your models here.
from .models import Article

# 将Article模型注册到admin后台
admin.site.register(Article)
