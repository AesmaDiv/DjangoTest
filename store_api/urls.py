from django.urls import path
from store_api.views import *

urlpatterns = [
    path('products/', ItemsListView.as_view()),
    path('products/create/', ItemCreateView.as_view()),
    path('products/<int:pk>/', ItemDetailView.as_view()),
]
