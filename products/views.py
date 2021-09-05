from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, SkillCategory, EnvCategory


def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    skill_categories = None
    env_categories = None

    if request.GET:
        if 'skill-category' in request.GET:
            skill_categories = request.GET['skill-category'].split(',')
            products = products.filter(skill_category__name__in=skill_categories)
            skill_categories = SkillCategory.objects.filter(name__in=skill_categories)

        if 'env-category' in request.GET:
            env_categories = request.GET['env-category'].split(',')
            products = products.filter(env_category__name__in=env_categories)
            env_categories = EnvCategory.objects.filter(name__in=env_categories)

        if 'searchq' in request.GET:
            query = request.GET['searchq']
            if not query:
                messages.error(request, "No search criteria was given.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {'products': products,
               'search_term': query,
               'curr_skill_categories': skill_categories,
               'curr_env_categories': env_categories, }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product, }

    return render(request, 'products/product_detail.html', context)
