from django import forms
from contact.models import Messages


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={"id": "name", "class": "form-control" "active", "placeholder": "Your name...", "autocomplete": "on"}
        )
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.TextInput(
            attrs={"id": "email", "class": "form-control" "active", "placeholder": "Your email...", "autocomplete": "on"}
        )
    )
    phone = forms.CharField(
        label="Phone",
        widget=forms.TextInput(
            attrs={"id": "phone", "class": "form-control" "active", "placeholder": "Your phone...", "autocomplete": "on"}
        )
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(
            attrs={"id": "message", "class": "form-control" "active", "placeholder": "Your message...", "autocomplete": "on"}
        )
    )

    def save(self, commit=True):
        data = self.cleaned_data
        msg = Messages(**data)
        if commit:
            return msg.save()
        return msg
