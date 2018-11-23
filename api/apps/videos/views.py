from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Video
from .serializers import VideoSerializer



class ListVideos(APIView):
    def get(self, request):
        videos = VideoSerializer(Video.objects.all(), many=True)
        return Response(videos.data)