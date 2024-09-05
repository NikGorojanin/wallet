import uuid

from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Wallet(BaseModel):
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField("Label", max_length=255, db_index=True, unique=True)
    balance = models.DecimalField("Balance", decimal_places=18, max_digits=30)


class Transaction(BaseModel):
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    wallet = models.ForeignKey(
        to=Wallet, related_name="transactions", on_delete=models.CASCADE
    )
    txid = models.CharField("TxID", max_length=255, unique=True)
    amount = models.DecimalField("Amount", decimal_places=18, max_digits=30)
