from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from products.models import Product
from .abstract import WritePaginatedAbstractView
from ..serializers import products
from products.services.create_product import create_product
from products.services.update_product import update_product


@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        request_body=products.ProductCreateUpdateBaseSerializer
    )
)
@method_decorator(
    name='update',
    decorator=swagger_auto_schema(
        request_body=products.ProductUpdateSerializer
    )
)
@method_decorator(
    name='partial_update',
    decorator=swagger_auto_schema(
        request_body=products.ProductPatchSerializer
    )
)
class ProductViewSet(WritePaginatedAbstractView):
    model = Product
    queryset = Product.objects.all()
    filter_fields = (
        'modified',
    )
    parser_classes = (MultiPartParser,)
    serializer_class = products.ProductDisplaySerializer
    permission_classes = [permissions.AllowAny, ]

    def create(self, request, *args, **kwargs):
        input_serializer = products.ProductCreateUpdateBaseSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        data = input_serializer.validated_data
        instance = create_product(
            name=data['name'],
            logo=data['logo'],
            description=data['description']
        )
        output_serializer = products.ProductDisplaySerializer(instance=instance)
        headers = self.get_success_headers(output_serializer.data)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        partial = kwargs.pop('partial', False)
        input_serializer = products.ProductUpdateSerializer(
            instance=instance,
            data=request.data,
            partial=partial
        )
        input_serializer.is_valid(raise_exception=True)
        data = input_serializer.validated_data
        instance = update_product(
            product=instance,
            **data
        )
        output_serializer = products.ProductDisplaySerializer(instance=instance)
        headers = self.get_success_headers(output_serializer.data)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
