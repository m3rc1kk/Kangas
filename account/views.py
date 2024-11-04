from django.http import HttpResponse

from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user_login = authenticate(username = user.username, password = form.cleaned_data['password'])

            if user_login is not None:
                if user_login.is_active:
                    login(request, user_login)
                    return HttpResponse('good')
                else:
                    return HttpResponse('Your account is disabled')
            else:
                return HttpResponse('Invalid login or password')
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {'form': form})
