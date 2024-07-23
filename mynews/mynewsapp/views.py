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


# Create your views here.

class NewsList(ListView):
    model = Article
    template_name = "index.html"
    paginate_by = 6
    

class AddNewsPost(CreateView):
    model = Article
    template_name = ''
    form_class = AddNewsForm


    def form_valid(self, form):
        author = Author.objects.get(user=self.request.user)
        form.instance.author = author
        form.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser

    def handle_no_permission(self):
        return HttpResponse("You are not an admin.")  


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


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, ("You were logged out!"))
    return redirect('home')

def home(request):
    return render(request, 'index.html')