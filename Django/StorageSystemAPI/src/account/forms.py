from account.models import Account
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=60)

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2", "name", "surname", "cell_phone", "phone", "address", "residence")


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login.")


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'username', 'name', 'surname', 'cell_phone', 'phone', 'address', 'residence')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']

            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account.email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']

            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % account.username)

    def clean_cell_phone(self):
        if self.is_valid():
            cell_phone = self.cleaned_data['cell_phone']

            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(cell_phone=cell_phone)
            except Account.DoesNotExist:
                return cell_phone
            raise forms.ValidationError('Cell phone number "%s" is already in use.' % account.cell_phone)