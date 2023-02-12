from django import forms
from .models import Member

class PostMember(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('firstName', 'lastName', 'email', 'phoneNumber', 'isAdmin')
