from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import EditProfile, LoginForm, SignupForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.template import loader
#from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    form = LoginForm()
    if request.user.is_authenticated:
        return redirect('profile') 
    #print('hello')
    if request.method == 'POST':
        #print('hello')
       
        form = AuthenticationForm(data=request.POST)
        #print(request.POST['username'])
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
        #print('hello')
    return render(request, 'login.html',{'form':form})

def signup(request):
    # Your sign-up logic here
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('signup')  # Redirect to a success page after signup
    else:
        form = SignupForm()
    return render(request, 'signup.html' , {'form': form})


def profile(request):
    user = request.user
    #user = Profile.objects.all().values()
    if request.user.is_authenticated:
        template = loader.get_template('profile.html')
        #print('hii')
        context = {
            'user' : user,
        }
        #print('hello')
        return HttpResponse(template.render(context, request))
    else:
        return redirect ('login')

def logout_view(request):
    logout(request)
    return redirect('login')
def edit_profile(request):
    print('hi')
    form = EditProfile()
    print('hello')


    #not working from here onwards



    if request.method == 'POST':
        print('hello')
       
        form = EditProfile(data=request.POST)
        print(request.POST['username'])
        if form.is_valid():
            user = form.get_user()
            print(user)
            login(request, user)
            return redirect('login')
        #print('hello')
    return render(request, 'edit_profile.html',{'form':form})

def master(request):
    template = loader.get_template('master.html')
    return HttpResponse(template.render())

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())