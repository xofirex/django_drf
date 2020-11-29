import pytest
from django.test.client import MULTIPART_CONTENT, encode_multipart, BOUNDARY
from django.urls import reverse

from products.models import Product

pytestmark = pytest.mark.django_db


def test_list(client, random_product):
    url = reverse('api:products-list')
    response = client.get(
        url,
        content_type='application/json',
    )
    assert response.status_code == 200
    assert response.data['count'] == 1


def test_detail(client, random_product):
    url = reverse('api:products-detail', kwargs={'pk': random_product.uuid})
    response = client.get(
        url,
        content_type='application/json',
    )
    assert response.status_code == 200
    assert response.data['uuid'] == str(random_product.uuid)


def test_post(client, create_fake_image):
    url = reverse('api:products-list')
    data = {
        'name': 'test',
        'logo': create_fake_image
    }
    response = client.post(
        url,
        data=data
    )
    assert response.status_code == 201
    assert Product.objects.count() == 1
    assert Product.objects.get().logo


def test_put(client, random_product, create_fake_image):
    url = reverse('api:products-detail', kwargs={'pk': random_product.uuid})
    create_fake_image.seek(0)
    data = {
        'name': 'new_name',
        'logo': create_fake_image
    }
    response = client.put(
        url,
        data=encode_multipart(BOUNDARY, data),
        content_type=MULTIPART_CONTENT
    )
    assert response.status_code == 201
    assert Product.objects.count() == 1
    assert Product.objects.get().name == data['name']


def test_patch(client, random_product):
    url = reverse('api:products-detail', kwargs={'pk': random_product.uuid})
    data = {
        'name': 'new_name'
    }
    response = client.patch(
        url,
        data=encode_multipart(BOUNDARY, data),
        content_type=MULTIPART_CONTENT
    )
    assert response.status_code == 201
    assert Product.objects.count() == 1
    assert Product.objects.get().name == data['name']


def test_second_edit_error(client, random_product):
    random_product.modified = True
    random_product.save(update_fields=['modified'])
    url = reverse('api:products-detail', kwargs={'pk': random_product.uuid})
    data = {
        'name': 'new_name'
    }
    response = client.patch(
        url,
        data=encode_multipart(BOUNDARY, data),
        content_type=MULTIPART_CONTENT
    )
    assert response.status_code == 400
    assert response.data['non_field_errors'][0] == 'Already edited.'


def test_delete(client, random_product):
    url = reverse('api:products-detail', kwargs={'pk': random_product.uuid})
    response = client.delete(url)
    assert response.status_code == 204
    assert not Product.objects.count()
