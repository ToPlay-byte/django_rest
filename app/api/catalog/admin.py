from django.contrib import admin
from django.utils.safestring import mark_safe

from mptt.admin import MPTTModelAdmin

from .models import Category, ImagesProduct, Product


admin.site.empty_value_display = 'Unknown'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    mptt_level_indent = 25


class ImagesInlineAdmin(admin.TabularInline):
    model = ImagesProduct
    max_num = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['get_img_banner', 'title', 'price']
    list_display_links = ['get_img_banner', 'title']
    search_fields = ['title']
    autocomplete_fields = ['categories']
    list_per_page = 5
    inlines = [ImagesInlineAdmin]

    def get_img_banner(self, obj):
        return mark_safe(f'<image width="70" height="70" src={obj.banner.url}/>')

