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


# 删除文章
class DeleteArticleView(View):
    def post(self, request, article_id):
        article = Article.objects.filter(pk=article_id).first()
        article.delete()
        return redirect("article:index")


# 编辑文章
class EditArticleView(View):
    def get(self, request, article_id):
        article = Article.objects.filter(pk=article_id).first()
        return render(request, 'article/edit_article.html', {'article': article})

    def post(self, request, article_id):
        article = Article.objects.filter(pk=article_id).first()
        article_form = ArticleForm(data=request.POST)
        if article_form.is_valid():
            article.title = article_form.cleaned_data['title']
            article.content = article_form.cleaned_data['content']
            article.save()
            return redirect("article:index")
        else:
            return HttpResponse("编辑文章失败")
