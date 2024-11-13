# Generated by Django 5.1.3 on 2024-11-08 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0015_category_article"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsletterSubscription",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("subscribed_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
