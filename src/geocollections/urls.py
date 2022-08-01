from django.conf.urls import url, include
  
from geonode.api.urls import router
from .views import GeocollectionDetail, GeocollectionViewSet

router.register(r'geocollections', GeocollectionViewSet, 'geocollections')

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$',
        GeocollectionDetail.as_view(),
        name='geocollection-detail'),
    url(r'^api/v2/', include(router.urls)),
]
