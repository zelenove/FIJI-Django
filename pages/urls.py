from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('brothers/', views.brothers, name='brothers'),
    path('faq/', views.faq, name='faq'),
]