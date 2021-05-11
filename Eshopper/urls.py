from django.urls import path, re_path

from . import views

app_name = 'Home'

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('category_item/<int:id>/', views.CategoryItem, name='CategoryItem'),
    path('product_detail/<int:id>/', views.ProductDetail, name='ProductDetail'),

]
