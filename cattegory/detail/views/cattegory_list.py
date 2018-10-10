from django_filters.rest_framework import DjangoFilterBackend

# from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
# from rest_framework.response import Response

# from rest_framework import authentication, permissions

from detail.models import Cattegory
from detail.serializers import CattegorySerializer


# class listCattegoryAPIView(APIView):
#     # authentication_classes = (authentication.TokenAuthentication,)
#     # permission_classes = (permissions.IsAdminUser,)

#     def get(self, request):
#         data = request.GET.copy()
#         serializer = CattegorySerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         filter_backends = (DjangoFilterBackend,)
#         filter_fields = ('species',)
#         return Response({'detail': serializer.data})


class ListCattegoryAPIView(ListAPIView):
    queryset = Cattegory.objects.all()
    serializer_class = CattegorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('species', 'price', 'food', 'buy_place')
