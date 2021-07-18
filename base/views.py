from django.shortcuts import render #, get_object_or_404
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.auth.models import User
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from .models import Post

def home(request):
    context = {
        'title': 'Home',
        # 'posts': Post.objects.all()
    }
    return render(request, 'base/home.html', context)

def about(request):
    return render(request, 'base/about.html', {'title': 'About'} )

def impressum(request):
    return render(request, 'base/impressum.html', {'title': 'Impressum'} )

def disclaimer(request):
    return render(request, 'base/disclaimer.html', {'title': 'Disclaimer'} )