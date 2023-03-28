from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_app, name='first_app'),
    path('page1/', views.page1, name='Page1'),
    path('compress/', views.compress, name='compress'),
    path('convert/', views.convert, name='convert'),
    path('merge/', views.merge, name='merge'),
   
]