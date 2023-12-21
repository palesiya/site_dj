from django import forms
from menu.models import PhotoBreakfast, PhotoDinner, PhotoLunch


# class PhotoForm(forms.ModelForm):
#     class Meta:
#         photo_menu = [PhotoBreakfast, PhotoDinner, PhotoLunch]
#         for photo in photo_menu:
#             model = photo
#             fields = ("img", "post")
#             # widgets = {"post": forms.HiddenInput()}
#
#
# class PhotoBreakfastF(forms.ModelForm):
#     class Meta:
#         model = PhotoBreakfast
#         fields = ("img", "post")
#         widgets = {"post": forms.HiddenInput()}
#
#
# class PhotoLunchF(forms.ModelForm):
#     class Meta:
#         model = PhotoDinner
#         fields = ("img", "post")
#         widgets = {"post": forms.HiddenInput()}
#
#
# class PhotoDinnerF(forms.ModelForm):
#     class Meta:
#         model = PhotoLunch
#         fields = ("img", "post")
#         widgets = {"post": forms.HiddenInput()}
