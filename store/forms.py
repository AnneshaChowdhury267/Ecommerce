from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			name = self.cleaned_data['username']
			email = self.cleaned_data['email']
			password = self.cleaned_data['password1']
			customer = Customer(user = user, name=name, email =email, password = password)
			user.save()
			customer.save()
		return user