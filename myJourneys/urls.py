from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('account', views.account, name='account'),
    path('register', views.register, name='register'),
    path('booking', views.booking, name='booking'),
    path('register', views.register, name='register' ),
    path('register/driver', views.register_driver, name='register_driver' ),
    path('register/successful', views.register_success, name='register_success' ),
]