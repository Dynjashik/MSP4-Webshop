from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import News


def all_news(request):
    """A view to show all news"""

    all_news = News.objects.all()
    context = {'news': all_news}

    return render(request, 'news/news.html', context)


@login_required
def add_news_item(request):
    """ Add news article """

    return redirect(reverse('news'))


@login_required
def edit_news_item(request, news_id):
    """ Edit news item """

    return redirect(reverse('news'))


@login_required
def delete_news_item(request, news_id):
    """ Delete news item """

    #if not request.user.is_superuser:
    #    messages.error(request, 'Sorry, only store owners can do that.')
    #    return redirect(reverse('home'))

    #product = get_object_or_404(Product, pk=product_id)
    #product.delete()
    #messages.success(request, 'Product deleted!')
    return redirect(reverse('news'))
