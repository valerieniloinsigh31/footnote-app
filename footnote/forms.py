from .models import FootNote, Idea
from django import forms
from .models import Idea


class FootNoteForm(forms.ModelForm):
    class Meta:
        model = FootNote
        fields = ('content',)


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('title', 'slug',
                  'content', 'featured_image',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder':
                                                'Pick a great title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder':
                                           'Lowercase version of title'}),
            'content': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder':
                                                 'Tell us your great idea'}),
        }
        