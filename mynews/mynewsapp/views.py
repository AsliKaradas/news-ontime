from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm, AddNewsForm, UpdateNewsForm
from mynewsapp.models import Article, Author
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm 
from .forms import SignUpForm 
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Article, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout


# Create your views here.

class NewsList(ListView):
    model = Article
    template_name = "index.html"
    paginate_by = 6
    

class AddNewsPost(CreateView):
    model = Article
    template_name = ''
    form_class = AddNewsForm
    template_name = 'add_news_post.html'
    success_url = '/home/'

    def form_valid(self, form):
        author = Author.objects.get(user=self.request.user)
        form.instance.author = author
        form.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser

    def handle_no_permission(self):
        return HttpResponse("You are not an Admin.")  

class Like(View):
    def post(self, request, slug, *args, **kwargs):
        news = get_object_or_404(Article, slug=slug)
        if news.likes.filter(id=request.user.id).exists():
            news.likes.remove(request.user)
        else:
            news.likes.add(request.user)

        return HttpResponseRedirect(reverse('article', args=[slug]))


class NewsDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(slug=slug)
        news = get_object_or_404(queryset, slug=slug)
        comments = news.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if news.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "article.html",
            {
                "article": news,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "form": CommentForm()
            },
        )
    def post(self, request, slug, *args, **kwargs):

        queryset = Article.objects.filter(published_status=1)
        news = get_object_or_404(queryset, slug=slug)
        comments = news.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if news.likes.filter(id=self.request.user.id).exists():
            liked = True

        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.instance.user = request.user
            comment = form.save(commit=False)
            comment.news = news
            comment.save()
        else:
            form = CommentForm()

        return render(
            request,
            "article.html",
            {
                "article": news,
                "comments": comments,
                "commented": True,
                "form": form,
                "liked": liked
            },
        )


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error logging in, please try again!"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})        


def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, "Your account has been created successfully!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request, 'index.html')

class UpdateNews(UpdateView):
    model = Article
    template_name = 'edit_news_post.html'
    form_class = UpdateNewsForm
    success_url = reverse_lazy('home')


class DeleteNews(DeleteView):
    model = Article
    template_name = 'delete_news_post.html'
    success_url = reverse_lazy('home')    