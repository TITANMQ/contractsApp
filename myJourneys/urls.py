from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard_user', views.dashboard_user, name='dashboard_user'),
    path('dashboard_driver', views.dashboard_driver, name='dashboard_driver'),
    path('account', views.account, name='account'),
    path('register', views.register, name='register'),
    path('bookings', views.bookings, name='bookings'),
    path('register', views.register, name='register' ),
    path('register/driver', views.register_driver, name='register_driver' ),
    path('register/successful', views.register_success, name='register_success' ),
]