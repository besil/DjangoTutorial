'''
Created on May 6, 2015

@author: besil
'''

from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        widgets = {
            'password': forms.PasswordInput(),
        }