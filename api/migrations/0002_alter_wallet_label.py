# Generated by Django 5.1 on 2024-09-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wallet",
            name="label",
            field=models.CharField(
                db_index=True, max_length=255, unique=True, verbose_name="Label"
            ),
        ),
    ]
