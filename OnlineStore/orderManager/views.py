from django.shortcuts import render
from django.http import HttpResponse
from orderManager.models import Articles

# Create your views here.
def search_articles(request):
  return render(request,"search_articles.html")

def search(request):
  if request.GET["articles_text"]:
    article=request.GET["articles_text"]
    articles=Articles.objects.filter(name__icontains=article)
    return render(request,"search_results.html",{"articles":articles,"query": article})
  else:
    message="value empty or not valid"
  return HttpResponse(message)