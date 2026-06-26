from django.urls import path

from .views import (
    ProductSearchView,
    ProductDetailView,
    ProductCategoryView
)

urlpatterns = [
    path(
        "search/",
        ProductSearchView.as_view()
    ),

    path(
        "category/<str:category>/",
        ProductCategoryView.as_view()
    ),

    path(
        "<int:product_id>/",
        ProductDetailView.as_view()
    ),
]