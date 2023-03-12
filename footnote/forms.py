from .models import FootNote
from django import forms

class FootNoteForm(forms.ModelForm):
    class Meta:
        model = FootNote
        fields = ('body',)
        
