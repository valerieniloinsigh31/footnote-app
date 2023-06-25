from .models import FootNote, Idea
from django import forms


class FootNoteForm(forms.ModelForm):
    class Meta:
        model = FootNote
        fields = ('content',)


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('content',)
