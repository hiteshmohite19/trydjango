from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from .forms import ArtileForm
from django.contrib.auth.decorators import login_required
from .models import Article


@login_required
def create_article(request):
    request_body = request.POST
    form = ArtileForm()

    data = {"isSaved": False, "form": form}

    if request.method == "POST":
        form_data = ArtileForm(request.POST or None)

        if form_data.is_valid():
            article = form_data.save()
            data["form"] = ArtileForm()
            data = {
                "isSaved": True,
                "data": article,
                "message": "Data saved, to add another click here",
            }

    return render(request, "articles/create_article.html", context=data)


@login_required
def search_article(request):
    query = request.GET

    articles = Article.objects.filter(title__icontains=query.get("query"))
    if not articles:
        return HttpResponse("404.html")

    content = {"articles": articles}

    return render(request, "articles/search_view.html", context=content)


# Create your views here.
@login_required
def article_detail_view(request, id=None):
    article = Article.objects.get(id=id)
    content = {"id": article.id, "title": article.title, "content": article.content}

    if not article:
        return Http404()

    return render(request, "articles/article.html", context=content)
