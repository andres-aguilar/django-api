from django.conf.urls import url

from .views import ListVideos

urlpatterns = [
    url(r'^videos/$', ListVideos.as_view(), name='list-videos'),
]