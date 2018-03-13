from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy


class HomeView(TemplateView):
    template_name = 'home.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


class LoginRequireMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequireMixin, cls).as_view(**kwargs)
        return login_required(view)
