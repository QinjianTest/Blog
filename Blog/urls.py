"""Blog URL Configuration

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
from BlogV1 import views
from django.urls import path, re_path

urlpatterns = [
    path('atxiyou/', admin.site.urls),

    path('', views.index),
    path('tech/', views.tech),
    path('testxmind/', views.testxmind),
    path('life/', views.life),
    path('about/', views.about),

    re_path(r'^article/(?P<nid>\d+)/', views.article),  # 文章详情页

]
