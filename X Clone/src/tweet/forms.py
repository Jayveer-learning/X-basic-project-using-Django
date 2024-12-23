from django import forms 
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta: # Meta class is used to specify the model that the form is going to use and provide the fields that we want to show in the form model. Meta class is used to provide the metadata of the form. 
        model = Tweet
        fields = ['text', 'photo']


class UserRegistraionForm(UserCreationForm):
    email = forms.EmailField() # if you want to create field in form you can do it by creating a field in the form but instance of models.field you have to use form.field. and then list in the Meta class. but best practice is create fields in models models.py file. 
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') # for build in fields we have to use tuple to specify the fields that we want to show in the form but for custom fields we can use list to specify the fields that we want to show in the forms medel. 

