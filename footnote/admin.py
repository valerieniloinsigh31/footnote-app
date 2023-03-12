from django.contrib import admin
from .models import Idea, FootNote
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Idea)
class IdeaAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')

