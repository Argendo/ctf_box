from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	username = forms.CharField(label=_('Login'))
	first_name = forms.CharField(label=_('First name'))
	last_name = forms.CharField(label=_('Last name'))
	password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
	password2 = forms.CharField(label=_('Password coniformation'), widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = (
			'username',
			'first_name', 
			'last_name',
			'email',
			'password1',
			'password2'
			)
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=True)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

		