from django.shortcuts import render
from django.views.generic import FormView
from contact.forms import ContactForm
from django.http import HttpResponseRedirect


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = "/contact/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

