# 引入path
from django.urls import path
# 引入views
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.ArticleView.as_view(), name='index'),
    path('<int:article_id>/', views.ArticleDetailView.as_view(), name='detail'),
    path('add_article/', views.AddArticleView.as_view(), name='add'),
    # 删除文章
    path('delete_article/<int:article_id>/', views.DeleteArticleView.as_view(), name='delete'),
    # 编辑文章
    path('edit_article/<int:article_id>/', views.EditArticleView.as_view(), name='edit'),

]
