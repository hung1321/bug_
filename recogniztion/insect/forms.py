from django import forms
from .models import guest
 
 
class Imageform(forms.ModelForm):
 
    class Meta:
        model = guest
        fields = ['image']