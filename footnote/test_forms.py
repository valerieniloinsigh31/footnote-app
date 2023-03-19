
from django.test import TestCase
from .forms import FootNoteForm

class TestFootNoteForm(TestCase):

    def test_item_name_is_required(self):
        form = footnote_form ({'name': ''})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = footnote_form()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
