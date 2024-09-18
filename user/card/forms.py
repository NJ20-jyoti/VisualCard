from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('id','username', 'email', 'password', 'nominee_name', 'mobile_number', 'dob', 'age', 'photo')