# Generated by Django 4.2.7 on 2023-11-17 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("secapp", "0003_profile"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="recipe",
            options={"ordering": ["-date_posted"]},
        ),
    ]
