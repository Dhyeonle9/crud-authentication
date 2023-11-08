from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request,'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    form = CommentForm()
    context= {
        'article': article,
        'form': form,
    }
    return render(request, 'detail.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            # 현재 로그인한 사람 정보를 넣어줌
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)

@login_required
def update(request, id):
    article = Article.objects.get(id=id)
    if request.user != article.user:
        return redirect('articles:detail', id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=id)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)
    

@login_required
def delete(request, id):
    article = Article.objects.get(id=id)
    if request.user == article.user:
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', id=id)

@login_required
def comment_create(request, id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article_id = id
        comment.save()
    return redirect('articles:detail', id=id)

@login_required
def comment_delete(request, id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', id=id)
    
