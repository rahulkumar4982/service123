from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, User

class SignupForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)
    full_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=200)
    class Otherfield:
       model = CustomUser
       fields = ['email', 'username', 'password','phone_number','full_name']
       widgets = {
            'password': forms.PasswordInput(),
        }
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)

class EditProfile(forms.Form):
    fullname = forms.CharField(max_length=255)
    email_id = forms.CharField(max_length=255)
    phone = forms.IntegerField()
    class edits:
        model = User
        fields = ['email', 'fullname', 'phone']
        
