from django.contrib import admin

from vendors.models import Shop, Category, Product, ProductInfo, Parameter, ProductParameter


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class ParameterAdmin(admin.TabularInline):
    model = Parameter


class ProductParameterInline(admin.TabularInline):
    model = ProductParameter


class ProductInfoInline(admin.TabularInline):
    model = ProductInfo
    inlines = (ParameterAdmin, ProductParameterInline,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductInfoInline,)
