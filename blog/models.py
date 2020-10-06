from django.db import models
from author.models import AuthorProfileModel
from tinymce.models import HTMLField
from django.urls import reverse

# Create your models here.
class ArticleModel(models.Model):
    class Meta:
        ordering = []
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        db_table = "articles"

    def get_article_image_path(self, file_name):
        extention = file_name.split(".")[-1]
        return str(self.author)+"/articles/"+self.title.replace(" ","_").replace(".","")+"."+extention

    title = models.CharField(max_length=200)
    overview = models.TextField(max_length=250)
    content = HTMLField()
    image = models.ImageField(upload_to=get_article_image_path, blank=True, null=True)
    author = models.ForeignKey(AuthorProfileModel, on_delete=models.CASCADE)
    category = models.ForeignKey('CategoryModel',on_delete=models.SET_NULL,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    @property
    def get_comments_count(self):
        return CommentModel.objects.filter(commented_on=self).count()

    def get_absolute_url(self):
        return reverse("post", kwargs={"id": self.id})
    
    def get_update_url(self):
        return reverse("article-update", kwargs={"id":self.id})
    
    def get_delete_url(self):
        return reverse("article-delete",kwargs={"id":self.id})
    

class CategoryModel(models.Model):
    class Meta:
        ordering = []
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "categories"

    name = models.CharField(max_length=30)
    created_by = models.ForeignKey(AuthorProfileModel, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def get_articles_count(self):
        return ArticleModel.objects.filter(category=self).count()

    def get_absolute_url(self):
        return reverse("category-articles", kwargs={"category": self.name.replace(" ","_")})
        
    

class CommentModel(models.Model):
    class Meta:
        ordering = []
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        db_table = "comments"

    comment = models.TextField()
    commented_by = models.ForeignKey(AuthorProfileModel, on_delete=models.CASCADE)
    commented_on = models.ForeignKey("ArticleModel", on_delete=models.CASCADE)
    date_commented = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

















    """ class HashtagModel(models.Model):
        class Meta:
            ordering = []
            verbose_name = "Hashtag"
            verbose_name_plural = "Hashtags"
            db_table = "hashtags"

        name = models.CharField(max_length=50)
        created_by = models.OneToOneField(AuthorProfileModel, null=True, on_delete=models.SET_NULL)
        date_created = models.DateTimeField(auto_now_add=True)
        date_modified = models.DateTimeField(auto_now=True)         """