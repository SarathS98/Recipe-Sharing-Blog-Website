# Generated by Django 4.2.7 on 2023-11-20 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("secapp", "0005_recipe_photo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="photo",
        ),
    ]
