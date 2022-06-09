import markdown
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
# 导入文章模型
from .models import Article
from .forms import ArticleForm


class ArticleView(View):
    def get(self, request):
        articles = Article.objects.all()
        # 返回HttpResponse对象
        return render(request, 'article/list.html', {'articles': articles})


class ArticleDetailView(View):
    def get(self, request, article_id):
        article = Article.objects.filter(pk=article_id).first()
        # 使用markdown语法渲染文章正文
        article.content = markdown.markdown(article.content,
                                            extensions=[
                                                # 包含 缩写、表格等常用扩展
                                                'markdown.extensions.extra',
                                                # 语法高亮扩展
                                                'markdown.extensions.codehilite',
                                                # 自动生成目录
                                                'markdown.extensions.toc',
                                            ])
        return render(request, 'article/detail.html', {'article': article})


# 使用forms来增加文章
class AddArticleView(View):
    def get(self, request):
        article_form = ArticleForm()
        return render(request, 'article/add_article.html', {'article_form': article_form})

    def post(self, request):
        article_form = ArticleForm(request.POST)
        print(article_form.is_valid())
        if article_form.is_valid():
            Article.objects.create(author_id=1, **article_form.cleaned_data)
            return redirect("article:index")
        else:
            # 返回错误信息
            return HttpResponse("发布文章失败")
