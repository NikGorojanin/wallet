from rest_framework import generics
from .serializers import TransactionSerializer
from api.models import Transaction
from .filters import TransactionsFilterBackend


class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.prefetch_related("wallet").order_by("-created_at")
    filter_backends = [TransactionsFilterBackend]


class TransactionsRetrieveView(generics.RetrieveAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
