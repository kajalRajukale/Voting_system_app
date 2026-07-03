from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Candidate, Vote


class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'id': 'login-username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-password'
        })
    )


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'photo', 'symbol', 'party', 'description', 'position', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'party': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Party Name (optional)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*', 'id': 'id_photo'}),
            'symbol': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*', 'id': 'id_symbol'}),
        }


class VoteForm(forms.Form):
    VOTER_ID_CHOICES = [
        ('student_id', 'Student ID'),
        ('mobile', 'Mobile Number'),
        ('voter_id', 'Voter ID'),
    ]

    voter_id_type = forms.ChoiceField(
        choices=VOTER_ID_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'voter-id-type'})
    )
    voter_id_value = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your ID',
            'id': 'voter-id-value'
        })
    )
    mobile_number = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mobile Number',
            'id': 'mobile-number'
        })
    )
    candidate_id = forms.IntegerField(
        widget=forms.HiddenInput(attrs={'id': 'candidate-id-input'})
    )
