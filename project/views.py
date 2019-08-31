from django.shortcuts import render,get_object_or_404
from slider.models import Slide
from django.db.models import Q
from project.models import Post
# Create your views here.

# def home(request):
    
#     return render(request, 'layouts/base.html')

def home(request):
    context = {
        'slides':Slide.objects.all(),
        'papers': Post.objects.filter(kind='pa')[:4],
        'news': Post.objects.filter(kind='ne')[:4],
        'journals': Post.objects.filter(kind='jo')[:4],
        'programs': Post.objects.filter(kind='pr')[:4]
    }
    return render(request, 'layouts/home.html',context)

def post_details(request,id):
    context = {
        'object':get_object_or_404(Post, id=id)
    }

    return render(request, 'layouts/post_details.html',context)


def post_list(request,kind):
    context = {
        'posts': Post.objects.filter(kind=kind),
    }
    return render(request, 'layouts/post_list.html',context)


def search(request):
    q=""
    if request.method == 'POST':
        q = (request.POST.get("q", ""))
        print(q)

        context = {
            'posts': Post.objects.filter(Q(title__icontains=q)|Q(description__icontains=q)),
        }
        return render(request, 'layouts/post_list.html',context)
