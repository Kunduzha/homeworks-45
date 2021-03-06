"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from webapp.views import list_view, add_list, list_more, list_update, delete_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_view, name='all_list'),
    path('add/', add_list, name='adding_list'),
    path('list/<int:pk>/', list_more, name='list_more'),
    path('delete/<int:pk>/', delete_list, name='delete_list'),
    path('update/<int:pk>/', list_update, name='list_update')
]
