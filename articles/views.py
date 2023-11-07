from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request,'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    context= {
        'article': article,
    }
    return render(request, 'detail.html', context)

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
def update(request, id):
    pass
def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')