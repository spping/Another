from django import forms
from .models import Bloger

class UserForm(forms.ModelForm):

    class Meta:
        model = Bloger
        fields = ('uname','upass')
        widgets = {
            'upass': forms.PasswordInput()
        }
    def clean(self):
        pass