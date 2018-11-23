from django.conf.urls import url

from .views import ListVideos, DetailVideo

urlpatterns = [
    url(r'^videos/$', ListVideos.as_view(), name='list-videos'),
    url(r'^videos/(?P<pk>[0-9]+)$', DetailVideo.as_view(), name='detail-video'),
]