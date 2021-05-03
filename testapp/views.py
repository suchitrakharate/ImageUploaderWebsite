from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import ListView ,CreateView,UpdateView,DeleteView
from testapp.models import Image
from testapp.models import Contact
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from django.contrib.auth.models import User 
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        contact=Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
    
    return render(request,'contact.html')


class ReadData(ListView):
    model=Image
 

class InsertData(CreateView):
    model=Image
    fields=('id','photo','caption')

class UpdateData(UpdateView):
    model=Image
    
    fields=('id','photo','caption')

class DeleteData(DeleteView):
    model=Image
    # fields=('id','photo','caption')

    success_url=reverse_lazy('home')



def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username) >10:
            messages.error(request,"username must be under 15 characters.")
            return redirect('index')
        
        if not username.isalnum():
            messages.error(request,"username should only contain letters and numbers.")
            return redirect('index')

        if pass1 != pass2:
            messages.error(request, "Password do not match.")
            return redirect('index')
        # Create the user
        # myuser = User.objects.create_user(username, email, pass1)
        # myuser.first_name= fname
        # myuser.last_name= lname
        # myuser.save()

        x=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=pass1)
        x.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('index')

    else:
        return HttpResponse("404 - Not found")


def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername,password=loginpassword)
       
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('index')

        else:
            messages.error(request,"Invalid Credentials ,Please try again.")
            return redirect('index')
    return HttpResponse('handleLogin')

def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('index')

    return HttpResponse('handleLogout')