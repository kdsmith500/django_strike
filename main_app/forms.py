# from django import forms
# from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import Profile

# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username')

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('user', 'image', 'bio')

# class BaseForm(ModelForm):
#   class Meta:
#     model = Base
#     fields = '__all__'