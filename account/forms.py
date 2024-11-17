from django import forms
from account.models import User
from django.forms import FileInput
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    avatar = forms.ImageField(widget=FileInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name' ,'password', 'password2', 'city', 'avatar')

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError('Имя пользователя занято')
        return data

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Почта уже занята')
        return data

    def clean_avatar(self):
        file = self.cleaned_data.get('avatar')
        if not file:
            raise ValidationError('Файл обязателен для загрузки')
        valid_extensions = ['png', 'jpg', 'jpeg']
        ext = file.name.split('.')[-1].lower()
        if ext not in valid_extensions:
            raise ValidationError('Допустимые форматы: PNG, JPG, JPEG')
        return file

class UserEditForm(forms.ModelForm):
    avatar = forms.ImageField(widget=FileInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name','city', 'avatar')

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError('Имя пользователя занято')

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Почта уже занята')
        return data

    def clean_avatar(self):
        file = self.cleaned_data.get('avatar')
        valid_extensions = ['png', 'jpg', 'jpeg']
        ext = file.name.split('.')[-1].lower()
        if ext not in valid_extensions:
            raise ValidationError('Вставьте картинку')
        return file