from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('logged in')
            else:
                return HttpResponse('invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user) #tworzy od razu profil uzytkownika
            return render(request, 'register_done.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})

@login_required
def edit(request): #edytujamy tutaj dwa formsy
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST) #instance potrzebne do edytowania,
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES) #files bo image
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)  #tutaj bez tego co wyzej bo uzytkownik jest juz zalogowany
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'edit.html', {'user_form': user_form, 'profile_form': profile_form})