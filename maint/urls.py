from django.urls import path

from . import views

app_name = 'maint'

urlpatterns = [
    # ex: /maint/
    path('', views.index, name='index'),
    # ex: /maint/3/
    path('<int:vehicle_id>/', views.detail, name='detail'),
    path('credit.html', views.credit, name='credit'),
]
