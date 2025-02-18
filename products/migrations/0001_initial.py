# Generated by Django 3.1.3 on 2020-11-29 14:15

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False,
                                          primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('logo', models.ImageField(upload_to='')),
                ('rotate_duration', models.DecimalField(decimal_places=6,
                                                        default=0.0, max_digits=20)),
                ('modified', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
