from api.models import Transaction
from rest_framework import serializers
from api.wallets.serializers import WalletSerializer
from api.models import Wallet
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist


class TransactionSerializer(serializers.ModelSerializer):
    wallet_id = serializers.UUIDField(required=True, write_only=True)
    wallet = WalletSerializer(read_only=True)

    def validate(self, data: dict):
        wallet_id = data.get("wallet_id")
        amount = data.get("amount")
        try:
            wallet = Wallet.objects.get(pk=wallet_id)
            if wallet.balance + amount < 0:
                raise serializers.ValidationError("Not enough balance in this wallet")
        except ObjectDoesNotExist:
            raise serializers.ValidationError(f"Wallet with id={wallet_id} does not exist")

        return data

    def create(self, validated_data):
        wallet_id = validated_data.get("wallet_id")
        amount = validated_data.get("amount")

        with transaction.atomic():
            wallet = Wallet.objects.select_for_update().get(pk=wallet_id)
            wallet.balance += amount
            wallet.save()
            transaction_instance = Transaction.objects.create(**validated_data)

        return transaction_instance

    class Meta:
        model = Transaction
        fields = "__all__"
