from django.contrib import admin
from django.utils.safestring import mark_safe
from products.models import Product, ProductOption, CartItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['photo_tag', 'description'] # 출력할 내용 설정
    list_display_links = ['description'] # 링크 설정

    def photo_tag(self, product):
        return mark_safe(f"<img src={product.image.url} style='width: 50px' />") #product.image.url #이미지 파일이 저장된 경로 출력


@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'size', 'color', 'stock_count']

    pass


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass


