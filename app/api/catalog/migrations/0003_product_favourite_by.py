# Generated by Django 4.2.7 on 2024-01-17 18:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0002_alter_product_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favourite_by',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourites', related_query_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
