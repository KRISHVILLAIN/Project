# Generated by Django 5.0.2 on 2024-03-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CRMS", "0005_user_registration_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_registration_model",
            name="password",
            field=models.CharField(default="pass", max_length=15),
        ),
        migrations.AlterField(
            model_name="user_registration_model",
            name="aadhar",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="user_registration_model",
            name="phone",
            field=models.IntegerField(),
        ),
    ]
