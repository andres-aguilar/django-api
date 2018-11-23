from django.shortcuts import render

from django.http import Http404

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
            

class DetailVideo(APIView):
    def get(self, request, pk):
        try:
            video = VideoSerializer(Video.objects.get(pk=pk))
            return Response(video.data)
        except Video.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        try:
            video = Video.objects.get(pk=pk)
            video_json = VideoSerializer(video, data=request.data)

            if video_json.is_valid():
                video_json.save()
                return Response(video_json.data)
            return Response(video.errors, status=400)

        except Video.DoesNotExist:
            raise Http404