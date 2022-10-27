from django.urls import path

from . import views

urlpatterns = [
    # ex: /maint/
    path('', views.index, name='index'),
    # ex: /maint/3/
    path('<int:vehicle_id>/', views.detail, name='detail'),
    

]
