from django import forms
from django.contrib.auth.models import User
from .models import Todo

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields=["first_name","last_name","username","email","password"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Firstname"}),
            "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"lastname"}),
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"username"}),
            "email":forms.TextInput(attrs={"class":"form-control","placeholder":"email"}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),
        }
class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        widgets={ 
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"username"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}),
        }

class TodoForm(forms.ModelForm):
    class Meta:
        model= Todo
        fields=["title","content"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Title"}),
            "content":forms.TextInput(attrs={"class":"form-control","placeholder":"content"}),
            

            }
        

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model= Todo
        fields=["title","content","status"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Title"}),
            "content":forms.TextInput(attrs={"class":"form-control","placeholder":"content"}),
            "status":forms.CheckboxInput(attrs={"class":"form-check-input","placeholder":"status"}),
            

            }
        