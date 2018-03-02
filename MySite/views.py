from django.views.generic import TemplateView
from django.conf import settings

class HomeView(TemplateView):
    template_name = 'home.html'
