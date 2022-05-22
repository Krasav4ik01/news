from dataclasses import field
from email.message import EmailMessage
from hashlib import new
from multiprocessing import context
from sre_constants import SUCCESS
from urllib import response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from . models import *
from .forms import *
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import admin_only, unauthenticated_user, allowed_users
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from .forms import SendForm


@unauthenticated_user
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('main')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
        
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('main')
			else:
				messages.info(request, 'Username OR password is incorrect')
                    
		context = {}
		return render(request, 'main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')


			messages.success(request, 'Account was created for ' + user)

			return redirect('logout')
			

	context = {'form':form}
	return render(request, 'main/register.html', context)





@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])

def index(request):
    
    if request.method == "POST":
        form = FileForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video-upload')
    else:
        form = FileForm()
        
    var = {'form': form}
    return render(request, 'main/index.html', var)




def main(request):
    var = Labours.objects.all()
    return render(request, 'main/main.html', {'var': var})




@login_required(login_url='login')
def heroes(request):
    inf = Heroes.objects.all()
    return render(request, 'main/heroes.html', {'inf2': inf})

# @login_required(login_url='login')
# def simple(request):
#     inf = Heroes.objects.all()
#     return render(request, 'main/simple.html', {'inf2': inf})

@login_required(login_url='login')
def writers(request):
    infw = Writers.objects.all()
    return render(request, 'main/writers.html', {'infw': infw})


@allowed_users(allowed_roles=['manager'])

def form(request):
    post = News.objects.all()
    return render(request, 'main/form.html', {'post': post})

@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])

def news_home(request):
    error = ' '
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new')
        else:
            error = 'Form was uncorrect'

    form = NewsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/news_home.html', data)






class NewsDetailView(DetailView):
    model = News
    template_name = 'main/details_view.html'
    context_object_name = 'article'
    
def show_detail(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)
    article = {'post':post}
    return render(request, 'main/details_view.html', context=article)


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'main/news_home.html'

    form_class = NewsForm
# def update_news(request, post_slug):
#     form = get_object_or_404(News, slug=post_slug)
    
#     return render(request, 'main/news_home.html', {'form': form})

def update_news(request, post_slug):
    order = News.objects.get(slug=post_slug)
    form = NewsForm(instance=order)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('new')
    context = {'form':form}
    return render(request, 'main/news_home.html', context)

def delete(request, post_slug):
    al = News.objects.get(slug=post_slug)
    al.delete()
    return redirect("new")


def forupload(request):
    video = Post.objects.all()

    return render(request, 'main/forupload.html', {'video' : video})

def userPage(request):
    context={}
    return render(request, 'main/user.html', context)

def managerPage(request):
    return render(request, 'main/manager.html')    


def contact(request):
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data.get('email')
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], '200103424@stu.sdu.edu.kz',[recipient], fail_silently=True)
            if mail:
                messages.success(request, 'Email is send!')
                return redirect('test')
            else:
                messages.error(request,'Sending error!')
        else:
            messages.error(request, 'Register error!')
    else:
        form=ContactForm()
    return render(request, 'main/contact.html', {'form':form})                        





#### views.py


# def subscribe(request):
#     form = SendForm()
#     if request.method == 'POST':
#         form = SendForm(request.POST)
#         if form.is_valid():
#             subject = 'Code Band'
#             message = 'Sending Email through Gmail'
#             recipient = form.cleaned_data.get('email')
#             send_mail(subject, 
#             message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
#             messages.success(request, 'Success!')
#             return redirect('contact')
#     return render(request, 'main/contact.html', {'form': form})




# def send_message(request):
#     email = EmailMessage(
#     "There is title", 
#     "There is content", 
#     "200103424@stu.sdu.edu.kz",
#     ["200103424@stu.sdu.edu.kz"],
#     headers={'Message-ID': 'foo'})
#     email.attach_file('')
#     email.send(fail_silently=False)
#     return render(request, 'main/labka.html')
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    # email = EmailMessage(
    # "There is title", 
    # "There is content", 
    # "200103424@stu.sdu.edu.kz",
    # ["200103424@stu.sdu.edu.kz"],
    # headers={'Message-ID': 'foo'})
    # email.attach_file('')
    # email.send(fail_silently=False)