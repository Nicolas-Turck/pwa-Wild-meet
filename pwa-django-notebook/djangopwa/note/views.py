from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,  logout
from .models import Encounter
from django.contrib.auth.decorators import login_required
from .forms import EncounterForm, SignUpForm, ContactForm
from django.http import HttpResponseRedirect
from django.core import serializers
import json
from django.contrib import sessions
import hashlib
from django.core.mail import EmailMessage
from django.template.loader import get_template



def signup(request):
    """form for registered new user of app"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            request.session['member_id'] = user.id
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'meet/signup.html', {'form': form})

def index(request):
    """method for show home page if user is registered
    else return login page
    i registred data for use page with offline mode"""
    #if 'member_id' in request.session:
    request.session['member_id'] = request.user.id
    cookies = request.session['member_id']
    if request.method == "GET":
        template='index.html'
        liste =Encounter.objects.all().order_by('-datetime')
        jsondata = serializers.serialize('json',liste)
        context={
                    'liste':liste,
                    'jsondata':jsondata,
                    'cookies': cookies,
                }
        return render(request,template,context)
    #else:
        #return render(request, 'note/login.html')

def getdata(request):
	liste=Encounter.objects.all()
	jsondata = serializers.serialize('json',liste)
	return HttpResponse(jsondata)

def base_layout(request):
	template='base.html'
	return render(request,template)

@login_required
def post_new(request):
    """display form for add new meet"""
    save = False
    if 'member_id' in request.session:
        cookies = request.session['member_id']
        if request.method == "POST":
            form = EncounterForm(request.POST or None, request.FILES)
            if form.is_valid():
                Encounter = form.save(commit=False)
                Encounter.user_id = cookies
                Encounter.save()
                save = True
                # liste = Encounter.objects.all()
                return render(request, 'index.html', {'cookies': cookies})
        else:
            form = EncounterForm()
            return render(request, 'meet/post_edit.html', {'form': form, 'save': save, 'cookies': cookies})
    """else:
        return render(request, 'meet/login.html', {'user': user})"""

@login_required
def liste(request):
    """display all object of user"""
    if 'member_id' in request.session:
        cookies = request.session['member_id']
        if request.method == "GET":
            liste = Encounter.objects.filter(user=cookies).order_by('-datetime')
            return render(request, 'meet/liste.html', {'liste': liste, 'cookies': cookies})
    """else:
         return render(request, 'meet/login.html')"""

@login_required
def fiche(request, pk):
    """display one fiche of bdd for action delette or modify"""

    if 'member_id' in request.session:
        cookies = request.session['member_id']
        #post = Encounter.objects.get(pk=pk)
        post = get_object_or_404(Encounter, pk=pk)
        #post = Encounter.objects.filter(pk=pk)
        return render(request, 'meet/fiche.html', {'post': post, 'cookies': cookies})
    """else:
        return render(request, 'meet/login.html')"""

@login_required
def guide(request):
    return render(request, 'meet/guide.html')

@login_required()
def post_edit(request, pk):
    post = get_object_or_404(Encounter, pk=pk)
    if 'member_id' in request.session:
        cookies = request.session['member_id']
        if request.method == "POST":
            form = EncounterForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                Encounter.user_id = cookies
                post.save()
                return render(request, 'meet/fiche.html', {'post': post})
        else:
            form = EncounterForm(instance=post)
        return render(request, 'meet/post_edit.html', {'form': form})


@login_required()
def post_del(request, pk):
    post = get_object_or_404(Encounter, pk=pk)
    if 'member_id' in request.session:
        cookies = request.session['member_id']
        if request.method == "POST":
            form = EncounterForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                Encounter.user_id = cookies
                post.delete()
                #messages.success(request, 'fiche supprimer ')
                return render(request, 'index.html')
        else:
            form = EncounterForm(instance=post)
        return render(request, 'meet/post_del.html', {'form': form})


def contact(request):
    """methof for user send email at dev"""
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['nicolas.turck@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('index')

    return render(request, 'meet/contact.html', {
        'form': form_class,
    })