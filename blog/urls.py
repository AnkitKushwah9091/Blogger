from django.urls import path
from .views import (
    get_index,
    get_articles,
    get_post,
    get_articles_by_category,
    get_search_result,
    get_article_create_view,
    get_article_update_view,
    get_article_delete_view,
    delete_comment,
    get_category_create_view,
    get_category_delete_view,
    get_category_update_view,
    )

urlpatterns = [
    path('', get_index , name="index"),
    path('articles', get_articles, name="articles"),
    path('article/<int:id>', get_post, name="post"),
    path('<slug:category>/articles', get_articles_by_category, name="category-articles"),
    path('search', get_search_result, name="search"),
    path('article/create', get_article_create_view, name="article-create"),
    path('article/<int:id>/update', get_article_update_view, name="article-update"),
    path('article/<int:id>/delete', get_article_delete_view, name="article-delete"),
    path('article/<int:aid>/comment/<int:cid>/delete', delete_comment, name="comment-delete"),
    path('category/create',get_category_create_view,name="category-create"),
    path('category/<int:id>/update',get_category_update_view,name="category-update"),
    path('category/<int:id>/delete',get_category_delete_view,name="category-delete"),

] 
