from django.shortcuts import render, HttpResponseRedirect, reverse
from . import models
from . import forms
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index_view(request):
    return render(request, 'index.html', {'movies': models.Movie.objects.all()})


def create_view(request):
    if request.method == "POST":
        form = forms.MovieForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_movie= models.Movie.objects.create(
                name = data['name'],
                parent = data['parent'],
            )
            if new_movie:
                return HttpResponseRedirect(reverse("homepage"))
    form = forms.MovieForm()
    return render(request, 'generic_form.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if user:
                login(request, user)
                # return HttpResponseRedirect(reverse('homepage'))
                return HttpResponseRedirect(request.GET.get( 'next',reverse('homepage')))
      
    form = forms.LoginForm()
    return render(request, 'generic_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
