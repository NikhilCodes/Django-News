from django.shortcuts import render
from django.apps import apps

ArticleModel = apps.get_model('article', 'Article')

# Create your views here.
def homepage_view(request, *arg, **kwargs):

    context = {
        "articleCollection": ArticleModel.objects.all(),
    }
    return render(request, 'home.html', context)
