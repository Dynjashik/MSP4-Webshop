from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import News


def all_news(request):
    """A view to show all news"""

    all_news = News.objects.all()
    context = {'news_in_html': all_news}

    return render(request, 'news/news.html', context)
