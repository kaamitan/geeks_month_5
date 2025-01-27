# Generated by Django 5.1.5 on 2025-01-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="stars",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
                null=True,
            ),
        ),
    ]
