from django.shortcuts import render
from django.http import Http404
from django.db import models
import uuid
from django.db.models import Sum
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from footnote.models import Idea, FootNote
from writer_profile.models import WriterProfile
from footnote.forms import FootNoteForm



class Medley(models.Model):
    content = models.TextField(max_length=280)
    
    def __str__(self):
        return self.title
