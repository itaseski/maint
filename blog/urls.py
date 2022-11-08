from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='home'),
    #path('<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
]