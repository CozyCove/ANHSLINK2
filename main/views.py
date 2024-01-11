from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import redirect
from .forms import PostForm
from .models import Post
# Create your views here.

def home (request):
    posts = Post.objects.all().order_by('-created_at')
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("anhs"))
    return render(request,"main/home.html", {"posts":posts})
def map(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("anhs"))
    return render(request,"main/map.html")
    
def history(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("anhs"))
    return render(request,"main/history.html")


def not_found(request, exception):
    response = render(request, 'main/404.html')
    response.status_code = 404
    return response

@login_required(login_url="/anhs")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()
    return render(request,"main/create_post.html", {"form":form})
