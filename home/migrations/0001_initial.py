# Generated by Django 4.2.7 on 2023-12-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BookTable",
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
                ("day", models.CharField(max_length=10, verbose_name="day")),
                ("hour", models.TimeField(verbose_name="hour")),
                ("name", models.CharField(max_length=30, verbose_name="name")),
                ("phone", models.CharField(max_length=10, verbose_name="phone")),
                ("person", models.CharField(max_length=10, verbose_name="person")),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Book_table",
                "verbose_name_plural": "Book_tables",
                "db_table": "Book_table",
            },
        ),
    ]