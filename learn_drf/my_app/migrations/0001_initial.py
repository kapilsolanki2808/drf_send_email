# Generated by Django 5.1.1 on 2024-09-24 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=120, null=True)),
                ("author", models.CharField(blank=True, max_length=130, null=True)),
            ],
        ),
    ]
