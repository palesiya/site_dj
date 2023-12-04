from django.db import models


class Messages(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=10, verbose_name="Phone")
    message = models.TextField(max_length=300, verbose_name="Message text")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "messages"
        verbose_name = "Message"
        verbose_name_plural = "Messages"
