from django import forms
from account.models import User
from django.forms import FileInput

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    avatar = forms.ImageField(widget=FileInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name' ,'password', 'password2', 'city', 'avatar')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name','city', 'avatar')