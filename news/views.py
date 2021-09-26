from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import News
from .forms import NewsForm
from datetime import datetime


def all_news(request):
    """A view to show all news"""

    all_news = News.objects.all().order_by("-date_added")
    context = {'news': all_news}
    return render(request, 'news/news.html', context)


@login_required
def add_news_item(request):
    """ Add news article """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added news article!')
            return redirect(reverse('news'))
        else:
            messages.error(request, 'Failed to news article. Please ensure the form is valid.')
    else:
        form = NewsForm()

    template = 'news/add_news.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_news_item(request, news_id):
    """ Edit news item """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    news_item = get_object_or_404(News, pk=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated "' + news_item.title + '" article!')
            return redirect(reverse('news'))
        else:
            messages.error(request, 'Failed to update "' + news_item.title + '" news article. Please ensure the form is valid.')
    else:
        form = NewsForm(instance=news_item)
        messages.info(request, f'You are editing "{news_item.title}" article')

    template = 'news/edit_news.html'
    context = {
        'form': form,
        'news_item': news_item,
    }
    return render(request, template, context)


@login_required
def delete_news_item(request, news_id):
    """ Delete news item """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    news_item = get_object_or_404(News, pk=news_id)
    deleted_title = news_item.title
    news_item.delete()
    messages.success(request, 'News article "' + deleted_title + '" deleted!')
    return redirect(reverse('news'))
