from rest_framework import generics
from store_api.serilizers import *


# Create your views here.
class ItemsListView(generics.ListAPIView):
    serializer_class = ItemListSerializer
    queryset = Product.objects.all()


class ItemCreateView(generics.CreateAPIView):
    serializer_class = ItemCreateSerilizer


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemCreateSerilizer
    queryset = Product.objects.all()
