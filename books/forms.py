from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import re

class RegistrationForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$', max_length=30, label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    first_name = forms.CharField( max_length=15, label=_("First Name"))
    last_name = forms.CharField( max_length=15, label=_("Last Name"))
    email = forms.EmailField(max_length=30, label=_("Email address"))
    password = forms.CharField(widget=forms.PasswordInput(), label=_("Password"))
    again_password = forms.CharField(widget=forms.PasswordInput(), label=_("Confirm Password"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password' in self.cleaned_data and 'again_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['again_password']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
    def save(self, commit=True):
        user = super(MyUserAdminForm, self).save
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$', max_length=30, label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    password = forms.CharField(widget=forms.PasswordInput(), label=_("Password"))
    def clean(self):
        return self.cleaned_data

class AddBookForm(forms.Form):

    title= forms.CharField(max_length=100, label=_("Title"))
    author= forms.CharField(max_length=30, label=_("Author"))
    publisher= forms.CharField(max_length=50, label=_("Publisher"))
    count= forms.IntegerField(label=_("Number of Copies"))

    def clean(self):
        return self.cleaned_data

class EditBookForm(forms.Form):

    title= forms.CharField(max_length=100, label=_("Title"))
    author= forms.CharField(max_length=30, label=_("Author"))
    publisher= forms.CharField(max_length=50, label=_("Publisher"))
    count= forms.IntegerField(label=_("Number of Copies"))
    bid=forms.IntegerField(widget=forms.TextInput(attrs={'readonly':'readonly'}),label=_("ID"))
    def clean(self):
        return self.cleaned_data