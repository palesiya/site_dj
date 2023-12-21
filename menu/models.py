from pathlib import Path
from django.db import models
from datetime import datetime
import random
from django.dispatch import receiver
from django.db.models.signals import post_delete


class Breakfast(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    price = models.FloatField()


class PhotoBreakfast(models.Model):
    def _load_to(self, filename):
        ext = filename.split(".")[-1]
        path = datetime.utcnow().strftime("Menu/Breakfast/%m.%Y/")
        f_b_name = hex(random.randint(100000, 999999))
        return f"{path}{f_b_name}.{ext}"

    img = models.ImageField(upload_to=_load_to)
    post = models.ForeignKey(Breakfast, on_delete=models.SET_NULL, null=True, related_name="images")
    loaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "breakfast_photo"


class Lunch(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    price = models.FloatField()


class PhotoLunch(models.Model):
    def _load_to(self, filename):
        ext = filename.split(".")[-1]
        path = datetime.utcnow().strftime("Menu/Lunch/%m.%Y/")
        f_b_name = hex(random.randint(100000, 999999))
        return f"{path}{f_b_name}.{ext}"

    img = models.ImageField(upload_to=_load_to)
    post = models.ForeignKey(Lunch, on_delete=models.SET_NULL, null=True, related_name="images")
    loaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "lunch_photo"


class Dinner(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    price = models.FloatField()


class PhotoDinner(models.Model):
    def _load_to(self, filename):
        ext = filename.split(".")[-1]
        path = datetime.utcnow().strftime("Menu/Dinner/%m.%Y/")
        f_b_name = hex(random.randint(100000, 999999))
        return f"{path}{f_b_name}.{ext}"

    img = models.ImageField(upload_to=_load_to)
    post = models.ForeignKey(Dinner, on_delete=models.SET_NULL, null=True, related_name="images")
    loaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "dinner_photo"


def clean_img(img_path: Path):
    try:
        img_path.unlink()
    except OSError:
        ...
    while True:
        img_path = img_path.parent
        try:
            img_path.rmdir()
        except OSError:
            break


Photo = [PhotoDinner, PhotoLunch, PhotoBreakfast]


@receiver(post_delete, sender=Photo)
def del_photo(sender, instance, **kwargs):
    img_path = Path(instance.img.path)
    clean_img(img_path)

