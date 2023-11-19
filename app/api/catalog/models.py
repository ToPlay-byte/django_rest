from mptt.models import MPTTModel, TreeForeignKey

from django.db import models


def upload_banner(obj, filename):
    return f'{obj.title}/{filename}'


def upload_images(obj, filename):
    return f'{obj.product.title}/{filename}'


class Product(models.Model):
    title = models.CharField(verbose_name='Title', max_length=69, unique=True)
    description = models.TextField(verbose_name='Description')
    banner = models.ImageField(verbose_name='Banner')
    price = models.DecimalField(verbose_name='Price', max_digits=10, decimal_places=2)
    quantity = models.IntegerField(verbose_name='Quantity')
    categories = models.ManyToManyField('Category', verbose_name='categories')
    characters = models.JSONField(verbose_name='Characters')

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-title']
        index_together = [
            ['title', 'price']
        ]
        default_related_name = 'products'

    def __str__(self):
        return str(self.title)


class Category(MPTTModel):
    name = models.CharField(verbose_name='Name', max_length=30, db_index=True, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ImagesProduct(models.Model):
    image = models.ImageField(verbose_name='Image', upload_to=upload_images)
    products = models.ForeignKey('Product', verbose_name='Select the product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images_product'
        verbose_name = 'Product`s image'
        verbose_name_plural = 'Product`s images'
        default_related_name = 'images'





