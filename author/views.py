from django.shortcuts import render,redirect,reverse
from .models import AuthorProfileModel
from django.contrib.auth.models import User
from blog.models import ArticleModel
from .forms import AuthorProfileForm,AuthorUserForm,AuthorPasswordChangeForm
# Create your views here.
def get_author_profile(request,id):
    author = AuthorProfileModel.objects.get(author__username = id) 
    form1 = AuthorUserForm(request.POST or None, instance=author.author) 
    form2 = AuthorProfileForm(request.POST or None,request.FILES or None, instance=author)
    form3 = AuthorPasswordChangeForm(request.POST or None)
    articles = ArticleModel.objects.filter(author = author)
    if request.method == "POST":
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()

        if form3.is_valid():
            form3.save()
        
        return redirect(reverse("author-profile",kwargs={
                'id':form1.instance.username,
            }))
           
    context={
        'author':author,
        'user':form1,
        'profile':form2,
        'password':form3,
        'articles':articles,
    }
    return render(request,"profile.html",context)

def get_delete_author(request,id):
    if request.method=="POST":
        author = User.objects.get(id=id)
        auth_profile=AuthorProfileModel.objects.get(author=author)
        author.delete()
    return redirect(reverse("index"))