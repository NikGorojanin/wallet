from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .wallets import views as wallet_views
from .transactions import views as tx_views

app_name = "api"


urlpatterns = [
    path("wallets", wallet_views.WalletListCreateView.as_view(), name="wallets"),
    path("wallets/<str:pk>", wallet_views.WalletRetrieveUpdateView.as_view()),
    path("transactions", tx_views.TransactionListCreateView.as_view()),
    path("transactions/<str:pk>", tx_views.TransactionsRetrieveView.as_view()),
]
