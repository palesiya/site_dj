from django.views.generic import ListView
from menu.models import Breakfast, Lunch, Dinner


class MenuView(ListView):
    model = Breakfast
    template_name = 'menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lunch"] = Lunch.objects.all()
        context["dinner"] = Dinner.objects.all()
        return context



