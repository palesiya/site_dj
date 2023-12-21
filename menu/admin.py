from django.contrib import admin
from menu.models import Breakfast, Lunch, Dinner, PhotoBreakfast, PhotoDinner, PhotoLunch


class MenuAdmin(admin.ModelAdmin):
    list_display = ("title", "price")


admin.site.register(Breakfast, MenuAdmin)
admin.site.register(Lunch, MenuAdmin)
admin.site.register(Dinner, MenuAdmin)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("img", "post")


admin.site.register(PhotoBreakfast, PhotoAdmin)
admin.site.register(PhotoDinner, PhotoAdmin)
admin.site.register(PhotoLunch, PhotoAdmin)
