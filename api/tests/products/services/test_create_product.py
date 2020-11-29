import pytest

from products.models import Product
from products.services.create_product import create_product

pytestmark = pytest.mark.django_db


def test_create_product(create_fake_image):
    assert not Product.objects.count()

    name = 'test_name'
    new_product = create_product(
        name=name,
        logo=create_fake_image
    )
    assert Product.objects.count() == 1
    assert new_product.name == name
