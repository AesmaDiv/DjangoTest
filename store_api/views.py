from rest_framework.response import Response
from rest_framework import generics
from store_api.serilizers import *


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.filter(deleted=False)


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

    def delete(self, request, *args, **kwargs):
        obj = Product.objects.get(id=kwargs['pk'])
        obj.deleted = True
        obj.save()
        return Response(self.get_serializer(obj).data)


class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.filter(deleted=False)


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategoryDetailSerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()

    def delete(self, request, *args, **kwargs):
        id_ = kwargs['pk']
        obj = Category.objects.get(id=id_)
        chains = Product.categories.through.objects.filter(category_id=id_)
        print(chains)
        if chains.count() > 0:
            ### ERROR
            serializer = ProductListSerializer(queryset=chains, many=True)
            return Response(serializer.data)
        obj.deleted = True
        obj.save()
        return Response(self.get_serializer(obj).data)
