from django import forms
from application3 import models
from django.contrib.auth import get_user_model
user=get_user_model()
class RegForm(forms.Form):
    fname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'First Name'
            }
        )
    )

    lname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Last Name'
            }
        )
    )

    user = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'User Name'
            }
        )
    )

    pwd = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )

    mobile = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email_Id'
            }
        )
    )

    dob = forms.CharField(
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
                'placeholder':'Date_Of_ Birth'
            }
        )
    )

    gender = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Gender'
            }
        )
    )


class LoginForm(forms.Form):
    user = forms.CharField(max_length=20)
    pwd = forms.CharField(widget=forms.PasswordInput())
