import uuid as uuid
from django.db import models

from .abstract_models import CreatedUpdatedModel


class Product(CreatedUpdatedModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    logo = models.ImageField()
    rotate_duration = models.DecimalField(max_digits=20, decimal_places=6, default=0.00)
    modified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.uuid} - {self.name}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
