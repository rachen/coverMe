from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


def login(request):
    next = request.GET['next'] if 'next' in request.GET else '/'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user and user.is_active:
            auth_login(request, user)

            return redirect('core.views.index')
        else:
            form.errors.update(errors="Your username or password is incorrect")
    else:
        form = AuthenticationForm()
    req_context = RequestContext(request, {"form": form, "next": next})
    return render_to_response('authentication/login.html', context_instance=req_context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            request.user = new_user
            return redirect('/')
    else:
        form = UserCreationForm()
    req_context = RequestContext(request, {"form": form})
    return render_to_response('authentication/register.html', context_instance=req_context)

def logout(request):
    auth_logout(request)
    return redirect('core.views.index')
