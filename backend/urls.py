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
from django.http import HttpResponse
from .Recommend.Recommend_Engine import get_top_n
import json


def myview(request):
    userId = request.GET.get('id', '')
    if userId != '':
        s_top_n = get_top_n.getRecommendResult(0, userId)
        c_top_n = get_top_n.getRecommendResult(1, userId)

        data = {
            "Scale": s_top_n,       
            "Compare": c_top_n
        }

        # for uid, user_ratings in top_n.items():
        #     data[uid] = [iid for (iid, _) in user_ratings]
        json_data = json.dumps(data)
        return HttpResponse(json_data)
    else:
        return HttpResponse("Error: No Id")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.Recommend.urls')),
    path('recommend/', myview),
]
