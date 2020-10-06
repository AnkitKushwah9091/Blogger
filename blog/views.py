from django.shortcuts import render,redirect,reverse
from django.db.models import  Q
from django.core.paginator import Paginator
from .models import ArticleModel,AuthorProfileModel,CategoryModel,CommentModel
from .forms import CommentForm,ArticleCreateForm,CategoryCreateForm
# Create your views here.
def get_index(request):
    articles = get_recent_articles()
    context={
        'articles':articles
    }
    return render(request, 'index.html',context)

def get_categories():
    return CategoryModel.objects.all()

def get_recent_articles():
    return ArticleModel.objects.order_by('-date_created')[:3]

def get_articles(request):
    articles = ArticleModel.objects.all()
    paginator = Paginator(articles,4) 
    page_no = request.GET.get('page') 
    articles = paginator.get_page(page_no)
    context = {
        'articles':articles,
        'categories':get_categories(),
        'recent_articles':get_recent_articles(),
    }
    return render(request, 'blogs.html', context)

def get_post(request,id):
    
    article = ArticleModel.objects.get(id=id)
    paginator = Paginator(article,1)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.commented_by = AuthorProfileModel.objects.get(author=request.user)
            form.instance.commented_on = article
            form.save()
            return redirect(reverse("post", kwargs={
                "id":id,
            }))
            
    context = {
        'article':article,
        'categories':get_categories(),
        'recent_articles':get_recent_articles(),
        'comment_form': form,
        'comments': CommentModel.objects.filter(commented_on__id=id)
    }
    return render(request, 'post.html',context) 

def get_articles_by_category(request,category):
    articles = ArticleModel.objects.filter(category__name=category)
    paginator = Paginator(articles,4)
    page_no = request.GET.get('page')
    articles = paginator.get_page(page_no)
    context = {
        'articles':articles,
        'categories':get_categories(),
        'recent_articles':get_recent_articles(),
    }
    return render(request, 'blogs.html', context)

def get_search_result(request):
    keywords = request.GET['q']
    if keywords:
        results = ArticleModel.objects.filter(Q(title__icontains=keywords)).distinct()
        print(results)
    context = {
        'results': results
    }
    return render(request, 'search_result.html', context)


def get_article_create_view(request):
    title = "Create Article"
    form = ArticleCreateForm(request.POST or None,request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = AuthorProfileModel.objects.get(author=request.user)
            form.save()
            return redirect(reverse("post",kwargs={
                'id':form.instance.id
            }))
    context ={
        'form':form,
        'title':title,
    }
    return render(request,"post_action.html",context)

def get_article_update_view(request,id):
    title = "Update Article"
    article = ArticleModel.objects.get(id=id)
    form = ArticleCreateForm(request.POST or None,request.FILES or None,instance=article)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("post",kwargs={
                'id':form.instance.id
            }))
    context ={
        'form':form,
        'title':title,
    }
    return render(request,"post_action.html",context)

def get_article_delete_view(request,id):
    title = "Delete Article"
    article = ArticleModel.objects.get(id=id)
    if request.method == "POST":
        article.delete()
        return redirect(reverse("articles"))

    context ={
        'article':article,
        'title':title,
    }
    return render(request,"post_action.html",context)

def delete_comment(request,cid,aid):
    comment = CommentModel.objects.get(id=cid)
    comment.delete()
    return redirect(reverse("post",kwargs={
        'id':aid
    }))
def update_comment(request):
    pass

def get_category_create_view(request):
    title = "Create Category"
    form = CategoryCreateForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.instance.created_by = AuthorProfileModel.objects.get(author=request.user)
            form.save()
        return redirect(reverse("index"))
    context = {
        "title":title,
        'form':form,
    }
    return render(request,"category.html",context)

def get_category_update_view(request,id):
    title = "Update Category"
    category = CategoryModel.objects.get(id=id)
    form = CategoryCreateForm(request.POST or None,instance=category)

    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect(reverse("index"))
    context = {
        "title":title,
        'form':form,
    }
    return render(request,"category.html",context)
 

def get_category_delete_view(request,id):
    title = "Delete Category"
    category = CategoryModel.objects.get(id=id)

    if request.method == "POST":
        category.delete()
        return redirect(reverse("index"))
    context = {
        "title":title,
        'id':id,
    }
    return render(request,"category.html",context)