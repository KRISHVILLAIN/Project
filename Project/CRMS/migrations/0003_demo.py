# Generated by Django 5.0.2 on 2024-03-22 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CRMS", "0002_rename_c_ac_register_model_c_am_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="demo",
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
                ("name", models.CharField(max_length=20)),
            ],
        ),
    ]
