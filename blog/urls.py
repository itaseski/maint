from django.urls import path

from.models import Post

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('post/<str:slug>/', views.PostsByCategory.as_view(), name='post'),
    path('category/<str:slug>/', views.get_category, name='category'),
]