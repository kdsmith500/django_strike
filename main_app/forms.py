from django.forms import ModelForm
from .models import User, Base

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('user', 'base_lat', 'base_lng')

# class BaseForm(ModelForm):
#   class Meta:
#     model = Base
#     fields = '__all__'