from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Order

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Register/Create a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create a record

class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Order
        fields =        fields = ['customer_email', 'customer_phone', 'product_category','product_name', 'product_quantity']



# - Update a record

class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Order
        fields =        fields = ['customer_email', 'customer_phone', 'product_category','product_name', 'product_quantity']
