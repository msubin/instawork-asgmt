from django.forms import ModelForm, TextInput, EmailInput, RadioSelect
from .models import Member
from django import forms


ROLES = [
    ('False', "Regular - Can't delete members"),
    ('True', 'Admin - Can delete members')
]


class MemberForm(ModelForm, forms.Form):
    isAdmin = forms.ChoiceField(choices=ROLES, widget=RadioSelect(attrs={'class': "form-check"}))

    class Meta:
        model = Member
        fields = "__all__"
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 100%; margin-bottom: 1rem',
                'placeholder': 'First Name'
            }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 100%; margin-bottom: 1rem',
                'placeholder': 'Last Name'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'width: 100%; margin-bottom: 1rem',
                'placeholder': 'Email'
            }),
            'phoneNumber': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 100%; margin-bottom: 1rem',
                'placeholder': 'Phone Number'
            }),
        }
