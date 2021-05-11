from django.contrib.auth.decorators import login_required
from django.urls import path, re_path

from . import views
from .views import BannerList


urlpatterns = [
path('banner/',views.ListBanner,name ='list_banner'),
path('add_banner/',views.BannerAdd,name='add_banner'),
path('update_banner/<int:id>',views.BannerManage,name='update_banner'),
path('delete_banner/<int:id>',views.BannerDelete,name='delete_banner'),
path('banner/', views.BannerList.as_view(), name='banner_list'),

]
