from django.contrib import admin
from .models import ArticleModel,CategoryModel,CommentModel
# Register your models here.

@admin.register(ArticleModel)
class ArticleModelAdmin(admin.ModelAdmin):
    pass

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    pass

@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    pass
