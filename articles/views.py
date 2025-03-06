from django.shortcuts import render, redirect
from .models import article
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from . import articleform
from django.utils.text import slugify
import uuid


# Create your views here.
def check_slug(request):
    slug = request.GET.get('slug', '')
    exists = article.objects.filter(slug=slug).exists()
    return JsonResponse({'exists': exists})


# def generate_unique_slug(title):
    base_slug = slugify(title)
    unique_slug = base_slug
    counter = 1
    
    while article.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{base_slug}-{counter}"
        counter += 1

    return unique_slug


def index(request):
    articles = article.objects.all().order_by('date')
    return render(request, 'articles/index.html', {'articles' : articles})


def article_details(request, slug):
    Article = article.objects.get(slug=slug)
    return render(request, 'articles/article-details.html', {'article':Article })

@login_required(login_url='accounts:login')
def create_article(request):
    if request.method == 'POST':
        form = articleform.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:home')
    else:
        form = articleform.CreateArticle()

    return render(request, 'articles/create.html', {'form': form})