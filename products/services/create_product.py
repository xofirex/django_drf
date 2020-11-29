from django.core.files.uploadedfile import InMemoryUploadedFile

from products.models import Product
from .process_image import rotate_image


def create_product(
    *,
    name: str,
    logo: InMemoryUploadedFile,
    description: str = ''
) -> Product:
    rotate_duration, logo = rotate_image(logo, 180)
    return Product.objects.create(
        name=name,
        description=description,
        logo=logo,
        rotate_duration=rotate_duration,
        modified=False
    )
