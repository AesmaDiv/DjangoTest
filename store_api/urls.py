from django.urls import path
from store_api.views import *

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/create/', ProductCreateView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),

    path('categories/', CategoryListView.as_view()),
    path('categories/create/', CategoryCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
]
