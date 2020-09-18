from django import forms
from .models import Encounter, User
from django.contrib.auth.forms import UserCreationForm
from django_countries.widgets import CountrySelectWidget
"""class UserappForm(forms.ModelForm):
    class Meta:
        model = Userapp
        fields = '__all__'"""


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


"""class EncounterForm(forms.ModelForm):

    class Meta:
        model = Encounter
        #fields = '__all__'
        fields = ['species', 'content', 'photo', 'locations']"""

class EncounterForm(forms.ModelForm):

    class Meta:
        model = Encounter
        #fields = '__all__'
        fields = ['title', 'types', 'biotopes', 'relief', 'content', 'photo', 'locations']


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)
        #widgets = {'country': CountrySelectWidget()}