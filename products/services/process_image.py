import time

from PIL import Image
from typing import Tuple

from django.core.files.uploadedfile import InMemoryUploadedFile


def rotate_image(image: InMemoryUploadedFile, angle: int) -> Tuple[float, InMemoryUploadedFile]:
    img = Image.open(image.file)
    start = time.time()
    img = img.rotate(angle, expand=True)
    rotate_duration = time.time() - start
    image.seek(0)
    img.save(image)
    return rotate_duration, image
