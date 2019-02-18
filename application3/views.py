from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import Reg
from .forms import LoginForm,RegForm

def home(request):
    return render(request,'home.html')

def reg(request):
    if request.method =='POST':
        form = RegForm(request.POST)

        if form.is_valid():
            fname = request.POST.get('fname','')
            lname = request.POST.get('lname','')
            user = request.POST.get('user','')
            pwd = request.POST.get('pwd','')
            mobile = request.POST.get('mobile','')
            email=request.POST.get('email','')
            dob = request.POST.get('dob','')
            gender = request.POST.get('gender','')

        reg = Reg(fname = fname,
                  lname = lname,
                  user = user,
                  pwd = pwd,
                  mobile = mobile,
                  email = email,
                  dob = dob,
                  gender = gender)
        reg.save()
        return HttpResponse('<h1>Registration Successful</h1>')

    else:
        form=RegForm()
        return render(request,'reg.html',{'form':form})

def login(request):

    if request.method =="POST":
        MyLoginForm = LoginForm(request.POST)

        if MyLoginForm.is_valid():
            user = MyLoginForm.cleaned_data['user']
            pwd = MyLoginForm.cleaned_data['pwd']
            dbuser = Reg.objects.filter(user=user)
            dbpwd = Reg.objects.filter(pwd = pwd)

            if dbuser and dbpwd:
                data = Reg.objects.get(fname='user')
                return render_to_response("retrieve.html", {'data': data})

            else:
                return HttpResponse('<h1>Login Failed</h1>')

        else:
            print(MyLoginForm.errors)

    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})







