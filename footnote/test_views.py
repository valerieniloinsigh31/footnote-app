from django.test import TestCase
from .models import Idea, FootNote
from django.shortcuts import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):  # Insert a test like this for all of the views in the project

    def test_get_idea_detail(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'footnote/idea_detail.html')
