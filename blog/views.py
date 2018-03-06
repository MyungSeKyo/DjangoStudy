from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from django.db.models import Q
from django.shortcuts import render
from blog.models import Post
from blog.forms import PostSearchForm


class PostLV(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 2


class PostDV(DetailView):
    model = Post


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        search_word = self.request.POST['search_word']
        post_list = Post.objects.filter(Q(content__icontains=search_word) |
                                        Q(description__icontains=search_word) |
                                        Q(content__icontains=search_word)).distinct()

        context = dict()
        context['form'] = form
        context['search_word'] = search_word
        context['object_list'] = post_list

        return render(self.request, self.template_name, context=context)
