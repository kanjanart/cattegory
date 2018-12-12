from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from detail.models import Cattegory
from detail.serializers import CattegorySerializer


class ListCattegoryAPIView(APIView):
    pagination_class = LimitOffsetPagination
    queryset = Cattegory.objects.all()

    def get(self, request):
        page = self.paginate_queryset(self.queryset)

        if page is not None:
            serializer = CattegorySerializer(page, many=True)
            return self.get_paginated_response({'detail': serializer.data})

        # return Response({'detail': serializer.data})
        # return self.get_paginated_response(serializer.data)

    @property
    def paginator(self):

        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()

        return self._paginator

    def paginate_queryset(self, queryset):

        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):

        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


# class ListCattegoryAPIView(ListAPIView):
#     queryset = Cattegory.objects.all()
#     serializer_class = CattegorySerializer
#     filter_backends = (DjangoFilterBackend,)
#     filter_fields = ('species', 'price', 'food', 'buy_place')