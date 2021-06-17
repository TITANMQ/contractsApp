from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/dashboard', views.dashboard_user, name='dashboard_user'),
    path('user/dashboard/cancel-booking', views.cancel_booking, name='cancel_booking'),
    path('driver/dashboard', views.dashboard_driver, name='dashboard_driver'),
    path('accept-booking/<int:booking_id>/<int:driver_id>', views.accept_booking , name='accept_booking'),
    path('account', views.account, name='account'),
    path('register', views.register, name='register'),
    path('bookings', views.bookings, name='bookings'),
    path('register', views.register, name='register' ),
    path('register/driver', views.register_driver, name='register_driver' ),
    path('register/successful', views.register_success, name='register_success' ),
    path('login', views.login, name='login' ),
    path('logout', views.logout, name='logout')
]