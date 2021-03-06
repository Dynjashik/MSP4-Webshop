from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, SkillCategory, EnvCategory
from .forms import ProductForm


def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    skill_cats = None
    env_cats = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            # force to sort categories by name instead of ids
            if sortkey == 'skill_category':
                sortkey == 'skill_category__name'
            if sortkey == 'env_category':
                sortkey == 'env_category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'skill-category' in request.GET:
            skill_cats = request.GET['skill-category'].split(',')
            products = (products.filter(skill_category__name__in=skill_cats)
                        .distinct())
            skill_cats = SkillCategory.objects.filter(name__in=skill_cats)

        if 'env-category' in request.GET:
            env_cats = request.GET['env-category'].split(',')
            products = (products.filter(env_category__name__in=env_cats)
                        .distinct())
            env_cats = EnvCategory.objects.filter(name__in=env_cats)

        if 'searchq' in request.GET:
            query = request.GET['searchq']
            if not query:
                messages.error(request, "No search criteria was given.")
                return redirect(reverse('products'))

            q = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(q)

    current_sorting = f'{sort}-{direction}'

    context = {'products': products,
               'search_term': query,
               'curr_skill_categories': skill_cats,
               'curr_env_categories': env_cats,
               'current_sorting': current_sorting, }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)
    skill_cats = product.skill_category.values()
    env_cats = product.env_category.values()

    context = {'product': product,
               'skill_categories': skill_cats,
               'env_categories': env_cats}

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           """Failed to add product. Please ensure the form
                              is valid.""")
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           """Failed to update product. Please ensure the form
                              is valid.""")
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
