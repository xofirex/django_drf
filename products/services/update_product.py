from products.models import Product
from .process_image import rotate_image


def update_product(
    *,
    product: Product,
    **data
) -> Product:
    logo = data.pop('logo', None)

    if logo:
        rotate_duration, logo = rotate_image(logo, 180)
        product.rotate_duration = rotate_duration
        product.logo = logo

    for key, value in data.items():
        setattr(product, key, value)

    product.modified = True
    product.save()

    return product
