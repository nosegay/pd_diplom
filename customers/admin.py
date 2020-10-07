from django.contrib import admin

from .models import Contact, Order, OrderItem


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    ordering = ('-dt',)
