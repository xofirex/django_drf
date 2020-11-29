from io import BytesIO

import pytest
from PIL import Image
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.fixture
def mock_django_file_storage(mocker):
    mocker.patch.object(
        FileSystemStorage,
        '_save',
        return_value='image.png'
    )


@pytest.fixture
def create_fake_image(mock_django_file_storage, settings):  # noqa
    data = BytesIO()
    image_name = 'image.png'
    Image.new('RGB', (40, 40)).save(data, 'PNG')
    data.filename = image_name
    data.seek(0)
    image_file = SimpleUploadedFile(
        image_name,
        data.getvalue(),
        content_type='image/png'
    )
    return image_file
