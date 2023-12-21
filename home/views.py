from django.shortcuts import render
from home.forms import BookTableForm, SignUpForm
from django.http import HttpResponseRedirect


def book_table(request):
    book_form = BookTableForm()
    sign_up = SignUpForm()
    if request.method == 'POST':
        book_form = BookTableForm(request.POST)
        sign_up = SignUpForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return HttpResponseRedirect(request.headers.get("Referer" or "/"))
        if sign_up.is_valid():
            sign_up.save()
            return HttpResponseRedirect(request.headers.get("Referer" or "/"))
    return render(request, 'home.html', {"form": book_form, "sign_up": sign_up})
