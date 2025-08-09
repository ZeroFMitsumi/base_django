from django.shortcuts import render

def home_view(request):
    context = {}
    return render(request, 'home.html', context)

def blog_template_view(request):
    context = {}
    return render(request, 'blog/home_blog.html', context)
