from django import forms 
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta: # Meta class is used to specify the model that the form is going to use and provide the fields that we want to show in the form model. Meta class is used to provide the metadata of the form. 
        model = Tweet
        fields = ['text', 'photo']