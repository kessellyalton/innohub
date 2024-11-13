# Generated by Django 5.1.3 on 2024-11-05 09:49

import django.utils.timezone
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(default="Untitled", max_length=200)),
                ("author", models.CharField(default="Anonymous", max_length=100)),
                (
                    "content",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Content"),
                ),
                (
                    "date_posted",
                    models.DateTimeField(blank=True, default=django.utils.timezone.now),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="blog_images/"),
                ),
            ],
            options={
                "ordering": ["-date_posted"],
            },
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(default="John Doe", max_length=100)),
                (
                    "email",
                    models.EmailField(default="example@example.com", max_length=254),
                ),
                ("subject", models.CharField(default="No Subject", max_length=200)),
                ("message", models.TextField(default="No message")),
                (
                    "created_at",
                    models.DateTimeField(blank=True, default=django.utils.timezone.now),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PDFFile",
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
                ("title", models.CharField(max_length=255)),
                ("file", models.FileField(upload_to="pdfs/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Resume",
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
                ("file", models.FileField(upload_to="uploads/")),
                (
                    "description",
                    models.CharField(
                        blank=True, default="No description provided", max_length=255
                    ),
                ),
                (
                    "uploaded_at",
                    models.DateTimeField(blank=True, default=django.utils.timezone.now),
                ),
            ],
        ),
    ]
