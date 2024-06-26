# Generated by Django 5.0.2 on 2024-03-23 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CRMS", "0007_delete_user_registration_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="user_registration_model",
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
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("username", models.CharField(max_length=20)),
                ("gender", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=50)),
                ("phone", models.IntegerField()),
                ("address", models.CharField(max_length=100)),
                ("aadhar", models.IntegerField()),
                ("password", models.CharField(default="pass", max_length=15)),
            ],
        ),
    ]
