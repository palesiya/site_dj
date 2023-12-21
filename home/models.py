from django.db import models


class BookTable(models.Model):
    day = models.CharField(max_length=10, verbose_name="day")
    hour = models.CharField(max_length=10, verbose_name="hour")
    name = models.CharField(max_length=30, verbose_name="name")
    phone = models.CharField(max_length=10, verbose_name="phone")
    person = models.CharField(max_length=10, verbose_name="person")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Book_table"
        verbose_name = "Book_table"
        verbose_name_plural = "Book_tables"


class SignUp(models.Model):
    email = models.EmailField(verbose_name="Email")

    class Meta:
        db_table = "sign_up"
