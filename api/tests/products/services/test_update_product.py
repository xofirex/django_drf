import pytest

from products.services.update_product import update_product

pytestmark = pytest.mark.django_db


def test_update_product(random_product):
    assert random_product.modified is False

    new_name = 'test_name'
    new_product = update_product(
        product=random_product,
        name=new_name
    )
    assert new_product.name == new_name
    assert new_product.modified is True
