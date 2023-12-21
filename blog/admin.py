from django.contrib import admin
from django.utils.safestring import mark_safe
from blog.models import Post, Photo


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date_posting")


admin.site.register(Post, PostAdmin)


class PhotoAdmin(admin.ModelAdmin):
    @staticmethod
    def full_img(obj):
        return mark_safe(f'img src="{obj.img.url}" width="300px" />')

    full_img.short_description = "Full image"
    list_display = ("img", "post", "loaded")
    list_filter = ("loaded",)
    readonly_fields = ("loaded", )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "img",
                    "post",
                    "loaded",
                )

            },
        ),
    )


admin.site.register(Photo, PhotoAdmin)
