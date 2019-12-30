from django.shortcuts import render,HttpResponse

from django.contrib import messages
# Create your views here.
from blog.models import Post
def home(request):
    return render(request,'home/home.html')


def search(request):
    query=request.GET['query']
    allpost=Post.objects.filter(title__icontains=query)
    params={'allpost':allpost}
    return render(request,'home/search.html',params)

