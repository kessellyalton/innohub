# Generated by Django 5.1.3 on 2024-11-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0012_alter_item_description_alter_post_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="testimonial",
            name="quote",
            field=models.TextField(),
        ),
    ]
