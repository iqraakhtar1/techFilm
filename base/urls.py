from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('text/', views.text, name='text'),
    path('voice/', views.voice, name='voice'),
    path('login/', views.login, name='login')
]

