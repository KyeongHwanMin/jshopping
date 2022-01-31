from django.urls import path

from products.views import ProductListAPIView, ProductDetailAPIView, ProductOptionListAPIView, ProductOptionDetailAPIView

urlpatterns = [
    path('Products/', ProductListAPIView.as_view()),
    path('Products/<int:pk>', ProductDetailAPIView.as_view()),
    path('productoptions/', ProductOptionListAPIView.as_view()),
    path('productoptions/<int:pk>', ProductOptionDetailAPIView.as_view()),
]
