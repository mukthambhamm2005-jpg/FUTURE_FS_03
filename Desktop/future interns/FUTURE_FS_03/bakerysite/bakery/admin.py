from django.contrib import admin
from .models import Product, Order, Contact, Testimonial ,CartItem ,Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    search_fields = ("name",)
    list_filter = ("category",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(Testimonial)
admin.site.register(CartItem)
admin.site.register(Category)