from rest_framework import filters
from decimal import Decimal


class TransactionsFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        txid = request.query_params.get("txid")
        amount_gte = request.query_params.get("amount_gte")
        amount_lte = request.query_params.get("amount_lte")
        wallet_id = request.query_params.get("wallet_id")
        wallet_label = request.query_params.get("wallet_label")

        if txid:
            queryset = queryset.filter(txid__icontains=txid)
        if amount_lte:
            queryset = queryset.filter(amount__lte=Decimal(amount_lte))
        if amount_gte:
            queryset = queryset.filter(balance__gte=Decimal(amount_gte))
        if wallet_id:
            queryset = queryset.filter(wallet_id=wallet_id)
        if wallet_label:
            queryset = queryset.filter(wallet__label__icontains=wallet_label)

        return queryset.all()
