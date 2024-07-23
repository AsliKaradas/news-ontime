from django import forms
from mynewsapp.models import Comment
from mynewsapp.models import Article, Author
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }
        help_texts = {
            'username': '',
            'password1': '',  
            'password2': '',
            'email': '',
        }

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Write a comment ...',
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ('content',)


class AddNewsForm(forms.ModelForm):
    news_overview = forms.CharField(widget=SummernoteWidget())
    news_content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Article
        fields = (
            'news_title', 'news_image', 'news_overview',
            'news_content')

        widgets = {
            'news_title': forms.TextInput(attrs={'class': 'form-control'}),
            'news_overview': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write content here ...',
            }),
            'news_content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write content here ...',
            }),
        }


class UpdateNewsForm(forms.ModelForm):
    news_overview = forms.CharField(widget=SummernoteWidget())
    news_content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Article
        fields = (
            'news_title', 'news_image', 'news_overview',
            'news_content')

        widgets = {
            'news_title': forms.TextInput(attrs={'class': 'form-control'}),
            'news_overview': forms.Textarea(attrs={'class': 'form-control'}),
            'news_content': forms.Textarea(attrs={'class': 'form-control'}),
        }