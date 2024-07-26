from .models import Women
from .serializers import WomanDetailSerializer
from rest_framework import viewsets


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomanDetailSerializer


# class WomenApiList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenApiUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomanApiDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomanDetailSerializer
#
# class WomenAPIView(APIView):
#
#     def get(self, request):
#         woman = Women.objects.all().values()
#         return Response({
#             "count": woman.count(),
#             "women": WomenSerializer(woman, many=True).data
#         }, status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data}, status.HTTP_201_CREATED)
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Not found"}, status.HTTP_404_NOT_FOUND)
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Not found"}, status.HTTP_404_NOT_FOUND)
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data}, status.HTTP_200_OK)
