from django import forms
from .models import CommentModel,ArticleModel,CategoryModel
from tinymce.widgets import TinyMCE
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('comment', )

    comment = forms.CharField(label='',widget=forms.Textarea(attrs={
        'placeholder': 'Type your comment',
        'rows': '4'
    }))


class ArticleCreateForm(forms.ModelForm):

    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    overview = forms.CharField(widget=forms.Textarea(attrs={
        'rows':'5'
    }))
    class Meta:
        model = ArticleModel
        fields = ('title','overview','content','image','category',)

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ('title','overview','content','image','category',)


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ('name',)