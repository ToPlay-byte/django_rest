from django.contrib import admin
from django.utils.safestring import mark_safe

from mptt.admin import MPTTModelAdmin

from .models import Category, ImagesProduct, Product


admin.site.empty_value_display = 'Unknown'


class CategoryAdmin(MPTTModelAdmin):
    search_fields = ['name']
    mptt_level_indent = 25


admin.site.register(Category, CategoryAdmin)


class ImagesInlineAdmin(admin.TabularInline):
    model = ImagesProduct
    max_num = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'banner']
    search_fields = ['title']
    autocomplete_fields = ['categories']
    list_per_page = 5

    def banner(self, obj):
        return mark_safe(f'<image src={obj.banner.url}/>')

