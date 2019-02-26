from django.conf.urls import url
from rest_framework_mongoengine import routers as merouters
from MoviesRecommendation.Recommend.views import TestViewSet,TitlesViewSet
 
merouter = merouters.DefaultRouter()
merouter.register(r'test', TestViewSet)
merouter.register(r'titles', TitlesViewSet)
 
urlpatterns = [
 
]
 
urlpatterns += merouter.urls