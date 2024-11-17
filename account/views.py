from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from .forms import UserForm, UserEditForm
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView

from .models import User


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
                    return redirect('main:product-list')
                else:
                    return HttpResponse('Your account is disabled')
            else:
                return HttpResponse('Invalid login or password')
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def user_edit(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserEditForm(instance=request.user)

    return render(request, 'account/user_edit.html', {"form": form})

class DetailProfileView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'account/profile.html'

    def dispatch(self, request, *args, **kwargs):
        user = self.get_object()
        if user != request.user:
            return redirect('profile', request.user.id)
        return super().dispatch(request, *args, **kwargs)