from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from django.contrib.auth.mixins import LoginRequiredMixin

# works as the dummy database
# posts = [
#     {
#         'author': 'kiran',
#         'title': 'blog 1',
#         'content': 'content 1',
#         'date_posted': '1 jan, 2077'
#     },
#     {
#         'author': 'xino',
#         'title': 'blog 4',
#         'content': 'content 8',
#         'date_posted': '8 aug, 5064'
#     }
# ]


# Create your views here.
def home(request):
    # return HttpResponse('<h1> Blog Home </h1>')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)  # rendering is happening


class PostListView(ListView):  # only setting the parameters to the class
    model = Post
    # <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):  # set the author of this post to current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    # return HttpResponse('<h1> Blog About </h1>')
    return render(request, 'blog/about.html', {'title': 'about it'})
