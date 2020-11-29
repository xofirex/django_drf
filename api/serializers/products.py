from collections import OrderedDict

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from products.models import Product


class ProductDisplaySerializer(serializers.ModelSerializer):
    logo = serializers.ReadOnlyField(source='logo.url')
    description = serializers.CharField(allow_blank=True, default='')

    class Meta:
        model = Product
        fields = (
            'uuid',
            'name',
            'description',
            'logo',
            'rotate_duration',
            'modified',
            'created',
            'updated',
        )
        read_only_fields = (
            'rotate_duration',
            'modified',
            'created',
            'updated',
        )


class ProductCreateUpdateBaseSerializer(ProductDisplaySerializer):
    logo = serializers.FileField()


class ProductUpdateSerializer(ProductCreateUpdateBaseSerializer):
    def validate(self, attrs):
        if self.instance.modified:
            raise ValidationError('Already edited.')
        return super().validate(attrs)


class ProductPatchSerializer(ProductUpdateSerializer):
    # Only for schema generation, not actually used.
    # because DRF-YASG does not support partial.
    logo = serializers.FileField(required=False)

    class Meta(ProductUpdateSerializer.Meta):
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False}
        }
