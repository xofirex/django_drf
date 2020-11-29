from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class PaginatedAbstractView:
    serializer_class = None
    pagination_class = StandardResultsSetPagination
    related_fields = []
    filter_backends = (
        DjangoFilterBackend,
    )
    filter_fields = '__all__'


class WritePaginatedAbstractView(PaginatedAbstractView, viewsets.ModelViewSet):
    pass
