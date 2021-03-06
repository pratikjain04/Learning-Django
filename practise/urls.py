"""practise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from learn import views
from django.contrib.auth.views import (login,
                                       logout,
                                       password_reset,
                                       password_reset_done,
                                       password_reset_confirm,
                                       password_reset_complete
                                        )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Homepage.as_view(), name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', login, {'template_name': 'learn/login.html'}, name='login'),
    path('logout/', logout, {'template_name': 'learn/logout.html'}, name='logout'),
    path('home/', views.Homepage_LoggedIn.as_view(), name='homepage_loggedIn'),
    path('home/edit/', views.edit_profile, name='edit_profile'),
    path('home/edit/changepassword', views.change_password, name='changepassword'),
    path('passwordreset/', password_reset, name='password_reset'),
    path('passwordreset/done/', password_reset_done, name='password_reset_done'),
    re_path('passwordreset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/', password_reset_confirm, name='password_reset_confirm'),
    path('passwordreset/complete/', password_reset_complete, name='password_reset_complete'),
]
