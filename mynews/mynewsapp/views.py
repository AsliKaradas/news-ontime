from django.shortcuts import render

# Create your views here.

def index(request):
    import requests
    import json

    news_api_request = requests.get("https://newsapi.org/v2/top-headlines?country=tr&apiKey=72b17a94e93944e881423cb6efd82bd4")
    api = json.loads(news_api_request.content)
    return render(request, 'index.html', {'api': api})    