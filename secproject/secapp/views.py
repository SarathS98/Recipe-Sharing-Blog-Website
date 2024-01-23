from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Recipe, Profile
from .forms import RecipesharingForm,UserUpdateForm
from django.views.generic import DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

posts = [
    {
        'author': 'Sreeraj',
        'title': 'Blog post 1',
        'content': 'This is my first blog post',
        'date_posted': '7th August 2021'
    },

    {
        'author': 'Abhinand',
        'title': 'Blog post 2',
        'content': 'This is a blog',
        'date_posted': '14th august 2021'
    }
]


def front_page(request):
    return render(request,'frontpage.html')

def about(request):
    return render(request,'about.html')

def log_in(request):
    
    if request.method == "POST":
        username = request.POST['usrnme']
        password = request.POST['pswrd']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            fname = user.username
            return redirect("/account/")
            return render(request, 'account.html', {'fname': fname})

        else:
            messages.error(request,'Bad credentials')
            return redirect('/joinpage/')
    return render(request,'login.html')

def join_pg(request):
    form = UserCreationForm()

    if request.method == "POST":
        username = request.POST.get('usrnme')
        email = request.POST.get('eml')
        password = request.POST.get('pswrd')

        myuser = User.objects.create_user(username,email,password)

        myuser.save()

        return redirect('lgin')
    return render(request,'joinpage.html')


def explore_pg(request):
    context = {
        'posts': Recipe.objects.all()
    }
    return render(request,'explore.html', context)

def profile_pg(request):
    if request.method == 'POST':
        form = RecipesharingForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.author = request.user
            author.save()
            return redirect('explr')
    else:
        form = RecipesharingForm()
    return render(request,'profile.html',{'form':form})


def account_pg(request):
    return render(request,'account.html')
    
    
class ArticleDetailView(DetailView):
    model = Recipe
    template_name = 'update.html'
    context_object_name = 'posts'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('explr')  
    template_name = 'explore.html' 
      
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['title', 'description']  
    template_name = 'profile.html'  
    success_url = reverse_lazy('explr') 
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
    
