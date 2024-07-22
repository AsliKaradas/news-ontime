from django.shortcuts import render, get_object_or_404
from .forms import CommentForm, AddNewsForm, UpdateNewsForm
from mynewsapp.models import Article, Author
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

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