"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework_mongoengine import routers as merouters

from backend.Recommend.views import (LinksViewSet, MoviesViewSet,
                                     RatingsViewSet, TagsViewSet,
                                     cRatingsViewSet, rMoviesViewSet)

merouter = merouters.DefaultRouter()
merouter.register(r'rm', rMoviesViewSet)
merouter.register(r'r', RatingsViewSet)
merouter.register(r'cr', cRatingsViewSet)
merouter.register(r'l', LinksViewSet)
merouter.register(r't', TagsViewSet)
merouter.register(r'm', MoviesViewSet)

urlpatterns = [

]

urlpatterns += merouter.urls
