from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from bookmark.models import Bookmark
from MySite.views import LoginRequireMixin


class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDV(DetailView):
    model = Bookmark


class BookmarkCreateView(CreateView, LoginRequireMixin):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookmarkCreateView, self).form_valid(form)


class BookmarkChangeLV(ListView, LoginRequireMixin):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class BookmarkUpdateView(UpdateView, LoginRequireMixin):
    model = Bookmark
    fields = ['title', ['url']]
    success_url = reverse_lazy('bookmark:index')


class BookmarkDeleteView(DeleteView, LoginRequireMixin):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')
