# Generated by Django 5.0.2 on 2024-03-17 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("CRMS", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="register_model",
            old_name="c_ac",
            new_name="c_am",
        ),
        migrations.RenameField(
            model_name="register_model",
            old_name="c_avg",
            new_name="c_price",
        ),
    ]
