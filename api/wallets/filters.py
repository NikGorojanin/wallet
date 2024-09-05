from rest_framework import filters
from decimal import Decimal


class WalletsFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        label = request.query_params.get("label")
        balance_gte = request.query_params.get("balance_gte")
        balance_lte = request.query_params.get("balance_lte")

        if label:
            queryset = queryset.filter(label__icontains=label)
        if balance_lte:
            queryset = queryset.filter(balance__lte=Decimal(balance_lte))
        if balance_gte:
            queryset = queryset.filter(balance__gte=Decimal(balance_gte))

        return queryset.all()
