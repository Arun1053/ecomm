from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError,transaction
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib import messages

from custom_admin.decorators import allowed_users
from django.views.generic import TemplateView


from .forms import *
from django.forms import inlineformset_factory
from django.utils.decorators import method_decorator



@login_required(login_url='custom_admin:login')
@allowed_users(allowed_roles=['admin'])
def ListBanner(request):

    banners= Banner.objects.all()

    return render(request,'banner/banner_list.html',{'banners':banners})



@login_required(login_url='custom_admin:login')
@allowed_users(allowed_roles=['admin'])
def BannerAdd(request):

    if request.method == 'POST':

        form = BannerForm(request.POST,request.FILES)

        if form.is_valid():

            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.modify_by = request.user
            instance.save()

            messages.success(request, 'banner updated succesfully')
            return redirect('banner_list')
    else:
        form = BannerForm()

    return render(request, 'banner/banner_form.html', {'form': form})


@login_required(login_url='custom_admin:login')
@allowed_users(allowed_roles=['admin'])
def BannerManage(request,id):

    bannerlists = get_object_or_404(Banner ,pk=id )

    if request.method == 'POST':
        form = BannerForm(request.POST,request.FILES,instance=bannerlists)
        print(form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.modify_by = request.user
            instance.save()

            messages.success(request,'banner updated succesfully')
            return redirect('banner_list')
    else:
        form = BannerForm(instance=bannerlists)

    return render(request, 'banner/banner_update.html', {'form': form,'id':id})



@login_required(login_url='custom_admin:login')
@allowed_users(allowed_roles=['admin'])
def BannerDelete(request,id):
    data = get_object_or_404(Banner ,pk=id)
    try:
        data.delete()
        messages.success(request,'banner is deleted succesfully')
    except IntegrityError:
        messages.warning(request,'bannerlist has banner ')


    return redirect('banner_list')


@method_decorator(login_required(login_url='custom_admin:login'), name='dispatch')
class BannerList(TemplateView):
    template_name = 'custom_admin/list/banner_list.html'
