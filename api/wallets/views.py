from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from api.wallets.serializers import WalletSerializer
from api.models import Wallet
from .filters import WalletsFilterBackend


class WalletListCreateView(ListCreateAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.order_by("-created_at")
    filter_backends = [WalletsFilterBackend]


class WalletRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()
