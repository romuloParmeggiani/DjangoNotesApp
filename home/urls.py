from django.urls import path

from . import views


urlpatterns = [
    # Replaced below function-base views by following class-based views
    # path('home', views.home),
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]