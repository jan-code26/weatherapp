from django.urls import path

from . import views

urlpatterns = [
    # path('signup',views.createuser.as_view(),name='signup'),
    # path('login',views.loginuser.as_view(),name='login'),
    # path('logout',views.logoutuser.as_view(),name='logout'),
    path('home', views.HomeView.as_view(),name='home'),
    
]