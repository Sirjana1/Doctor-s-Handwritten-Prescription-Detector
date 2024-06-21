"""
URL configuration for HTD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from HTDapp import views

urlpatterns = [
    # path("",views.index1, name='index'),
    # path("", views.custom_login, name="login"),
     path('', views.index, name='index'),

    # path("welcome", views.welcome, name='welcome'),
    # path("login_view", views.login_user, name="login_view"),
    path("register/", views.register, name="register"),
    # path('register/', views.register, name='register'),
     path('login_view/', views.login_view, name='login_view'),
    # path('logout/', views.custom_logout, name='logout'),
    # path('upload', views.upload, name='upload'),
    # path('', views.index_view, name='index_view'),
    # # path('predict', views.predict_view, name='predict_view'),
    # path('', views.abc, name = 'abc'),
]

  



