# Generated by Django 4.2.7 on 2023-12-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Messages",
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
                ("name", models.CharField(max_length=30, verbose_name="Name")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("phone", models.CharField(max_length=10, verbose_name="Phone")),
                (
                    "message",
                    models.TextField(max_length=300, verbose_name="Message text"),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Message",
                "verbose_name_plural": "Messages",
                "db_table": "messages",
            },
        ),
    ]
