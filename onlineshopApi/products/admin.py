from django.contrib import admin
from .models import (
    Category,
    Product,
    Brand,
    Color,
)


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ['id', 'name', 'name', 'slug', 'date_created']
    exclude = ('description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Brand)
admin.site.register(Color)
