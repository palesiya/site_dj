# Generated by Django 4.2.7 on 2023-12-11 14:41

from django.db import migrations, models
import django.db.models.deletion
import menu.models


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="breakfast",
            name="img",
        ),
        migrations.RemoveField(
            model_name="dinner",
            name="img",
        ),
        migrations.RemoveField(
            model_name="lunch",
            name="img",
        ),
        migrations.CreateModel(
            name="PhotoLunch",
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
                ("img", models.ImageField(upload_to=menu.models.PhotoLunch._load_to)),
                ("loaded", models.DateTimeField(auto_now_add=True)),
                (
                    "post",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="images",
                        to="menu.lunch",
                    ),
                ),
            ],
            options={
                "db_table": "lunch_photo",
            },
        ),
        migrations.CreateModel(
            name="PhotoDinner",
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
                ("img", models.ImageField(upload_to=menu.models.PhotoDinner._load_to)),
                ("loaded", models.DateTimeField(auto_now_add=True)),
                (
                    "post",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="images",
                        to="menu.dinner",
                    ),
                ),
            ],
            options={
                "db_table": "dinner_photo",
            },
        ),
        migrations.CreateModel(
            name="PhotoBreakfast",
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
                (
                    "img",
                    models.ImageField(upload_to=menu.models.PhotoBreakfast._load_to),
                ),
                ("loaded", models.DateTimeField(auto_now_add=True)),
                (
                    "post",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="images",
                        to="menu.breakfast",
                    ),
                ),
            ],
            options={
                "db_table": "breakfast_photo",
            },
        ),
    ]
