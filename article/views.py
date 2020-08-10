from django.shortcuts import render
from .models import Article
# Create your views here.
def articlepage_view(request, id, *args, **kwargs):
  article = Article.objects.get(id=id)
  context = {"article": article}
  return render(request, 'article/article.html', context)
