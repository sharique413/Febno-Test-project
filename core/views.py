from django.shortcuts import redirect, render
from django.views.generic import View
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return render(request,'core/home.html')

class SignupView(View):
    def get(self, request):
        fm= SignUpForm()
        return render(request, 'core/signup.html',{'form': fm})

    def post(self, request):
        fm = SignUpForm(request.POST)
        print(fm)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Sign Up Success !")
            return redirect('/login')
        else:
            print(fm.errors)
            return render(request, 'core/signup.html', {'form': fm})

class MyloginView(View):
    def get(self, request):
        fm= MyLoginForm
        print(fm)
        return render(request, 'core/login.html', {'form': fm})

    def post(self, request):
        fm = MyLoginForm(request, data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            
            user = authenticate(request, username=username , password= password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'core/login.html', {'form':fm})
        else:
            return render(request, 'core/login.html',{'form':fm})
