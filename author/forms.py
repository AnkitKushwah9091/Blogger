from django import forms

from django.contrib.auth.models import User
from .models import AuthorProfileModel
class AuthorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name')



class AuthorProfileForm(forms.ModelForm):
    class Meta:
        model = AuthorProfileModel
        fields = ('birth_date','gender','contect_no','profile_pic',)
    
    birth_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

class AuthorPasswordChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('password',)

    password = forms.CharField(widget=forms.widgets.PasswordInput())
        