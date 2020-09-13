from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
import datetime
from django.shortcuts import render , get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView




def current_datetime(request):
    now = datetime.datetime.now()
    html = ("<html>"""
            "<title>hello</title>"""
            "<head>myweb</head>"""
            "<body>the time is now %s "
            "<p>this is a paragraph<p>"
            ""
            ""
            ""
            ""
            ""
            ""
            ""
            "</body>""</html>" % now)
    return HttpResponse(html)


def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def home(request):    # home function view
    context={
        'post':Post.objects.all()
    }
    return render(request,'home.html',context)


class PostListView(ListView): # home class based view
    model = Post
    template_name = 'mywebsite/home.html'
    context_object_name = 'post'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):  # home class based view
    model = Post
    template_name = 'mywebsite/user_post.html'
    context_object_name = 'post'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView): # home class based view
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView): # home class based view
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin , UpdateView):  # home class based view
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView): # home class based view
    model = Post
    success_url = '/'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'about.html')


def music(request):
    contexts={
        'MUSICIANS':MUSICIANS
    }
    return render(request, 'music.html', contexts)


MUSICIANS = [

{'name': 'Django Reinhardt', 'genre': 'jazz'},
{'name': 'Jimi Hendrix', 'genre': 'rock'},
{'name': 'Louis Armstrong', 'genre': 'jazz'},
{'name': 'Pete Townsend', 'genre': 'rock'},
{'name': 'Yanni', 'genre': 'new age'},
{'name': 'Ella Fitzgerald', 'genre': 'jazz'},
{'name': 'Wesley Willis', 'genre': 'casio'},
{'name': 'John Lennon', 'genre': 'rock'},
{'name': 'Bono', 'genre': 'rock'},
{'name': 'Garth Brooks', 'genre': 'country'},
{'name': 'Duke Ellington', 'genre': 'jazz'},
{'name': 'William Shatner', 'genre': 'spoken word'},
{'name': 'Madonna', 'genre': 'pop'},

]
