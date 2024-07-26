from django.forms import model_to_dict
from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Women
from .serializers import WomenSerializer
import json

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


class WomenAPIView(APIView):

    def get(self, request):
        woman = Women.objects.all().values()
        return Response({"status": list(woman)}, status.HTTP_200_OK)

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            cat_id=request.data["cat_id"]
        )
        return Response({"post":model_to_dict(post_new)}, status.HTTP_201_CREATED)
