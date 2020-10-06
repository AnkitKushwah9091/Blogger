from django.contrib import admin
from .models import AuthorProfileModel
# Register your models here.

@admin.register(AuthorProfileModel)
class AuthorProfileModelAdmin(admin.ModelAdmin):
    pass
