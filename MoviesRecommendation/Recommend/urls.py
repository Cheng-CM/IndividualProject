from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from MoviesRecommendation.Recommend.views import TitlesViewSet
 
merouter = merouters.DefaultRouter()
merouter.register(r'titles', TitlesViewSet)
 
urlpatterns = [
 
]
 
urlpatterns += merouter.urls