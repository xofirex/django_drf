import pytest

from products.models import Product

pytestmark = pytest.mark.django_db


@pytest.fixture
def random_product(create_fake_image):
    return Product.objects.create(
        name='test name',
        description='test description',
        logo=create_fake_image,
        rotate_duration=0.1,
        modified=False
    )
