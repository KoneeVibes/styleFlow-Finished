from django.urls import path

from . import views


app_name = 'home' 

urlpatterns = [
    path('', views.home, name='home'),                       # the website's homepage
    path('faq', views.faq, name='faq'),                      # the FAQ page
]