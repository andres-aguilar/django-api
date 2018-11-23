from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Video
from .serializers import VideoSerializer



class ListVideos(APIView):
    def get(self, request):
        videos = VideoSerializer(Video.objects.all(), many=True)
        return Response(videos.data)

    def post(self, request):
        video = VideoSerializer(data=request.data)

        if video.is_valid():
            video.save()
            return Response(video.data, status=201)
        
        return Response(video.errors, status=400)
            
