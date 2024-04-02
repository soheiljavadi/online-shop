from django.contrib import admin
from django.contrib import admin
from .models import product, Category, Comment, Question, Answer,\
    Image, ProductOption, SellerProductPrice, Brand

# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = Image
    extra = 1


class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    extra = 1


class ProductPriceInline(admin.TabularInline):
    model = SellerProductPrice
    extra = 1

@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'Category']
    list_filter = ['Category', 'is_active']
    search_fields = ['en_name', 'name']
    inlines = (ProductImageInline, ProductOptionInline, ProductPriceInline)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'parent']
    list_filter = ['parent']
    search_fields = ['name', 'description']
    fieldsets = (
        ('details', {
            'fields': ('name', 'slug', 'parent',
                       ('description',),)
        }),
        ('images', {
            'fields': ('icon', 'image',)
        }),

    )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'rate', 'title']