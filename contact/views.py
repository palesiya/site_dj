from django.shortcuts import render
from contact.forms import ContactForm
from django.http import HttpResponseRedirect


def contact(request):
    cform = ContactForm()
    if request.method == 'POST':
        cform = ContactForm(request.POST)
        if cform.is_valid():
            cform.save()
            return HttpResponseRedirect(request.headers.get("Referer" or "/"))
    return render(request, 'contact.html', {"form": cform})
