from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
# Create your models here.

class AuthorProfileModel(models.Model):
    class Meta:
        ordering = []
        verbose_name = "Author Profile"
        verbose_name_plural = "Authors Profiles"
        db_table = "authors_profiles"

    GENDERS = [ ('M','Male'),('F','Female'),('O','Other'),]

    def get_author_image_path(self, file_name):
        extention = file_name.split(".")[-1]
        return str(self.author)+"/profile/"+self.author.username+"."+extention


    author = models.OneToOneField(User,on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, default="M", choices=GENDERS)
    contect_no = models.CharField(max_length=15, blank=True,null=True)
    profile_pic = models.ImageField(upload_to=get_author_image_path , default="default.jpeg",blank=True, null=True)

    def __str__(self):
        return self.author.username

   
    

@receiver(post_save, sender=User)
def author_profile_model(sender, instance, created, **kwargs):
    if created:
        AuthorProfileModel.objects.create(author=instance)
        