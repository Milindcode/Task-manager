"""firstPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from firstApp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', ViewTask.as_view()),
    path('creation/', CreateTask.as_view()),
    path('update/<pk>/', UpdateTask.as_view()),
    path('delete/<pk>/', DeleteTask.as_view()),
    path('signup/', SignUp.as_view()),
    path('login/', Login.as_view()),
    path('logout/', LogoutView.as_view()),
]