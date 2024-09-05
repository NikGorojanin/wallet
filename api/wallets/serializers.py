from rest_framework import serializers

from api.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(max_digits=30, decimal_places=18, min_value=1.0)

    class Meta:
        model = Wallet
        fields = "__all__"

    def update(self, instance, validated_data):
        if "balance" in validated_data:
            raise serializers.ValidationError(
                {"balance": ["Balance can't be updated via PATCH request."]}
            )
        return super().update(instance, validated_data)
