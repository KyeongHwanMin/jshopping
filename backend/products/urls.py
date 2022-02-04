from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from products.views import ProductListAPIView, ProductDetailAPIView, ProductOptionListAPIView, ProductOptionDetailAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>', ProductDetailAPIView.as_view()),
    path('productoptions/', ProductOptionListAPIView.as_view()),
    path('productoptions/<int:pk>', ProductOptionDetailAPIView.as_view()),
]
