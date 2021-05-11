from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, AnonymousUser
from django.contrib.auth import get_user_model



from django import template
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from custom_admin.forms import RegisterForm

from custom_admin.models import Product, ProductImage, Categories
from banner.models import Banner

from django.core.paginator import Paginator

#User = get_user_model()


def index(request):
    products = Product.objects.all().order_by('-name')
    banners = Banner.objects.filter(banner_name='Home')
    categories = Categories.objects.all()
    product_images = ProductImage.objects.filter(product__is_featured__icontains=True)

    paginator = Paginator(products, 4)
    products = paginator.page(1)

    return render(request, 'Eshopper/index.html', {'banners': banners,'products': products,
                                                   'product_images': product_images, 'categories': categories, })





def login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        valuenext = request.POST.get('next')

        user = authenticate(request, username=username, password=password)

        if user is not None and valuenext == '':
            # import pdb
            # pdb.set_trace()
            auth_login(request, user)
            messages.success(request, 'you are logged in')
            return redirect('Home:index')
        elif user is not None and valuenext != '':
            auth_login(request, user)
            return redirect(valuenext)
        else:
            messages.warning(request, 'please enter valid credential')

    form = RegisterForm()
    return render(request, 'Eshopper/frontend/login.html', {'form': form, })



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            form = form.save()
            default_group = Group.objects.get(name='customer')
            form.groups.add(default_group)
            form.save()

            messages.success(request, 'Your profile was successfully created!')
            return redirect('Home:login')
    else:
        form = RegisterForm()
    return render(request, 'Eshopper/frontend/login.html', {
        'form': form,
    })




@login_required(login_url='Home:login')
def logoutUser(request):
    logout(request)
    return redirect('Home:login')


def CategoryItem(request, id):
    banners = Banner.objects.filter(banner_name='Home')
    categories = Categories.objects.all()

    products = Product.objects.filter(product_categories__id=id).order_by('-created_date')
    product_images = ProductImage.objects.filter(product__product_categories__id=id).order_by('-created_date')

    paginator = Paginator(products, 4)
    products = paginator.page(1)

    id = id

    return render(request, 'Eshopper/frontend/category_item.html',
                  {'products': products, 'categories': categories, 'id': id,
                   'banners': banners, 'product_images': product_images})


def ProductDetail(request, id):
    product = Product.objects.get(id=id)
    categories = Category.objects.all()
    product_images = ProductImage.objects.filter(product=product)
    for product_image in product_images:
        print(product_images.image_name)

    return render(request, 'Eshopper/frontend/product_detail.html',
                  {'product_images': product_images, 'product': product, 'categories': categories})
