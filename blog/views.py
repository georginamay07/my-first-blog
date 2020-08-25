from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import CV
from .forms import PostForm
from .forms import CVForm
from django.shortcuts import redirect
from django.forms import formset_factory 


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def homepage(request):
    return render(request, 'blog/homepage.html')
    
def cv(request):
    cv = CV.objects.all()[:1].get()
    return render(request, 'blog/cv.html', {'cv': cv})

def cv_edit(request):
    cv = CV.objects.all()[:1].get()
    if request.method == "POST":
        form = CVForm(request.POST, request.FILES, instance=cv)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.author = request.user
            cv.save()
        return render(request, 'blog/cv.html', {'cv':cv})
    else:
        form = CVForm(instance=cv)
    return render(request, 'blog/cv_edit.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})