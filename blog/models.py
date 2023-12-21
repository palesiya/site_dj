import enum
from pathlib import Path
from django.db import models
from datetime import datetime
import random
from django.dispatch import receiver
from django.db.models.signals import post_delete


class Author(enum.StrEnum):
    CHEF = "C"
    ADMINISTRATOR = "A"
    OWNER = "O"


class Post(models.Model):
    AUTHOR = (
        (Author.CHEF, "Chef"),
        (Author.ADMINISTRATOR, "Admin"),
        (Author.OWNER, "Owner")
    )

    author = models.CharField(max_length=1, choices=AUTHOR)
    title = models.CharField(max_length=100)
    date_posting = models.CharField(max_length=15, blank=True)
    topic = models.CharField(max_length=20)
    text = models.TextField()

    class Meta:
        db_table = "post"


class Photo(models.Model):

    def _load_to(self, filename):
        ext = filename.split(".")[-1]
        path = datetime.utcnow().strftime("blog/%m.%Y/")
        f_b_name = hex(random.randint(100000, 999999))
        return f"{path}{f_b_name}.{ext}"

    img = models.ImageField(upload_to=_load_to)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name="images")
    loaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "photo"


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


@receiver(post_delete, sender=Photo)
def del_photo(sender, instance, **kwargs):
    img_path = Path(instance.img.path)
    clean_img(img_path)

