from django.shortcuts import render
# from appTwo.models import User
from appTwo.forms import NewUserForm,UserForm,UserProfileInfoForm
from . import forms

#
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context_dict = {"text":"hello world","number":100}
    return render(request, 'appTwo/index.html',context_dict)

@login_required
def special(request):
    return HttpResponse("you are logged in, Nice")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active")
        
        else:
            print("Someone tried to login and failed")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("invalid login details supplied")
    
    else:
        return render(request,'appTwo/logins.html',{})



def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'appTwo/registration.html',
                                        {'registered':registered,
                                        'profile_form':profile_form,
                                        'user_form':user_form})


def other(request):
    return render(request,"appTwo/other.html")

def relative(request):
    return render(request,"appTwo/relative_url_templates.html")



def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("error form valid")
    return render(request,"appTwo/users.html",{"form":form})

    # user_list = User.objects.order_by('first_name')
    # user_dict = {'users':user_list}
    # return render(request,'appTwo/users.html',context=user_dict)

def form_name_view(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            #Do sonething code
            print("validation success")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    return render(request,'appTwo/form_page.html',{'form':form})