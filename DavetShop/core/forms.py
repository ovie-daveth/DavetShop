from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, AdminPasswordChangeForm


class LoginForm(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control',
         'autocomplete': 'off'
    }))
     password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control',
        'type': 'password',
         'autocomplete': 'off'
    }))

class registerForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "username", "password1", "password2")
    
    def save(self, commit=True):
        user = super(registerForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'form-control'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'form-control'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control',
        'autocomplete': 'off'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control',
         'type': 'email'
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control',
        'type': 'password',
        'autocomplete': 'off'
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Comfirm Password',
        'class': 'form-control',
        'type': 'password'
    }))

# class loginForm(AuthenticationForm):
#     class Meta:
#         models = User
#         fields = ('username')