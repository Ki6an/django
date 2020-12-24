from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post


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
    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1> Blog About </h1>')
    return render(request, 'blog/about.html', {'title' : 'about it'})
