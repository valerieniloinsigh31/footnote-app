from django.contrib import admin
from .models import Idea, FootNote
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Idea)
class IdeaAdmin(SummernoteModelAdmin):

    list_display = ('title','slug','status','created_on')
    search_fields = ['title','content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')

@admin.register(FootNote)
class FootNoteAdmin(admin.ModelAdmin):

    list_display = ('name','body','idea','created_on','approved')
    list_filter = ('approved','created_on')
    search_fields =('name','email','body')
    actions = ['approve footnotes']

    def approve_footnotes(self, request, queryset):
        queryset.update(approved=True)
