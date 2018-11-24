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
    def _get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        video = VideoSerializer(self._get_object(pk))
        return Response(video.data)

    def put(self, request, pk):
        video = VideoSerializer(self._get_object(pk), data=request.data)

        if video.is_valid():
            video.save()
            return Response(video.data)
        return Response(video.errors, status=400)

    def delete(self, request, pk):
        video = self._get_object(pk)
        video.delete()
        return Response(status=200)
