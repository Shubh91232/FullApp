# Generated by Django 4.2.2 on 2023-07-12 09:50

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tree",
            fields=[
                (
                    "Tree_id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("qrcode_id", models.CharField(max_length=255)),
                ("TreeName", models.CharField(max_length=255)),
                ("TreeDatile", models.TextField()),
            ],
        ),
    ]