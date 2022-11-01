from django.urls import path

from . import views


app_name = 'fasteners'
urlpatterns = [

    path('', views.screws, name='screws'),
    
    path('din933/', views.din933, name='din933'),
    path('din933/<int:din933_id>/', views.din933_detail, name='din933_detail'),

    path('din931/', views.din931, name='din931'),
    path('din931/<int:din931_id>/', views.din931_detail, name='din931_detail'),

    path('din6921/', views.din6921, name='din6921'),
    path('din6921/<int:din6921_id>/', views.din6921_detail, name='din6921_detail'),

    path('din912/', views.din912, name='din912'),
    path('din912/<int:din912_id>/', views.din912_detail, name='din912_detail'),

    path('din7981/', views.din7981, name='din7981'),

    path('iso14583/', views.iso14583, name='iso14583'),

    path('din7500D/', views.din7500D, name='din7500D'),
   

]