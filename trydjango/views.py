from django.http import HttpResponse
from articles.models import Article
import random
from django.template.loader import render_to_string


  


def home(request):
    articles = Article.objects.all()

    content = {
        "articles":articles
    }

    HTML_STRING = render_to_string("home.html", context=content)

    return HttpResponse(HTML_STRING)
