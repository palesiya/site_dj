from django import forms
from home.models import BookTable, SignUp


class BookTableForm(forms.Form):
    day = forms.ChoiceField(choices=((1, "Select day"),
                                     (2, "Monday"),
                                     (3, "Tuesday"),
                                     (4, "Wednesday"),
                                     (5, "Thursday"),
                                     (6, "Friday"),
                                     (7, "Saturday"),
                                     (8, "Sunday")))
    hour = forms.ChoiceField(choices=((1, "Select hour"),
                                      (2, "10:00"),
                                      (3, "12:00"),
                                      (4, "14:00"),
                                      (5, "16:00"),
                                      (6, "18:00"),
                                      (7, "20:00"),
                                      (8, "22:00")))
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"id": "name", "class": "form-control" "active", "placeholder": "Full name", "autocomplete": "on"}
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={"id": "phone", "class": "form-control" "active", "placeholder": "Phone number",
                   "autocomplete": "on"}
        )
    )
    person = forms.ChoiceField(choices=((1, "How many persons?"),
                                        (2, "1-Person"),
                                        (3, "2-Persons"),
                                        (4, "3-Persons"),
                                        (5, "4-Persons"),
                                        (6, "5-Persons"),
                                        (7, "6-Persons")))

    def save(self, commit=True):
        data = self.cleaned_data
        bt = BookTable(**data)
        if commit:
            return bt.save()
        return bt


class SignUpForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"id": "email", "class": "form-control" "active", "placeholder": "Your email...",
                   "autocomplete": "on"}
        )
    )

    def save(self, commit=True):
        data = self.cleaned_data
        bt = SignUp(**data)
        if commit:
            return bt.save()
        return bt
