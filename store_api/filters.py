from django_filters import rest_framework as filters
from store_api.models import Product


class CategoryFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilterSet(filters.FilterSet):
    # id = filters.Filter()
    name = filters.CharFilter(lookup_expr='contains')
    category_id = CategoryFilter(field_name='categories__id', lookup_expr='in')
    category_name = CategoryFilter(field_name='categories__name', lookup_expr='in')
    price = filters.Filter()
    # posted = filters.Filter()
    # deleted = filters.Filter()

    class Meta:
        model = Product
        fields = ['id', 'name', 'categories', 'price', 'posted', 'deleted']
