from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
# 导入文章模型
from .models import Article


class ArticleView(View):
    def get(self, request):
        articles = Article.objects.all()
        # 返回HttpResponse对象
        return render(request, 'article/list.html', {'articles': articles})
