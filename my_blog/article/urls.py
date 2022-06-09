# 引入path
from django.urls import path
# 引入views
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.ArticleView.as_view(), name='index'),
]
