from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class RegistrationForm(UserCreationForm):
	username = forms.CharField(label=_('Login'))
	email = forms.EmailField(required=True)
	password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
	password2 = forms.CharField(label=_('Password coniformation'), widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = (
			'username',
			'email',
			'password1',
			'password2'
			)
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=True)
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

		