from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('login1/', views.login1, name='login1'),
    path('logout1/', views.logout1, name='logout1'),
]
