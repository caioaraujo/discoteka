from django.shortcuts import render
from rest_framework.views import APIView


class Album(APIView):

    def post(self, request):
        pass

    def get(self, request):
        pass


class AlbumId(APIView):

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
