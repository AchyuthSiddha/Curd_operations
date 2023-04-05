"""CurdOperations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Insertion_Topic/',Insertion_Topic,name='Insertion_Topic'),
    path('Insertion_Webpage/',Insertion_Webpage,name='Insertion_Webpage'),
    path('Insertion_AccessRecord/',Insertion_AccessRecord,name='Insertion_AccessRecord'),
    path('Display_Topic/',Display_Topic,name='Display_Topic'),
    path('Display_Webpage/',Display_Webpage,name='Display_Webpage'),
    path('Display_AccesRecord/',Display_AccesRecord,name='Display_AccesRecord'),
]

