from django import forms
from .models import WriterProfile


class WriterProfileForm(forms.ModelForm):

    class Meta:
        model = WriterProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {

            'email': 'email',
            'default_gender': 'Gender',
            'default_default_town_or_city': 'Town or city',
            'default_writingtype': 'Writing Style',
            'default_genre': 'Favourite genre',
            'default_favouriteauthor': 'Fave writer',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'writerprofile-form-input'
            self.fields[field].label = False
