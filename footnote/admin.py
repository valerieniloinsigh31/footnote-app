from django.contrib import admin
from .models import Idea, FootNote
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Idea)
class IdeaAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    actions = ['approve ideas'] #ADDED THIS FOR CRUD...may remove edit, delete, add
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')

    def approve_ideas(self, request, queryset):
        queryset.update(approved=True)

    #def add_ideas(self, request, queryset):
        #queryset.update(approved=True)
    
    #def delete_ideas(self, request, queryset):
        #queryset.update(deleted=True)

    #def edit_ideas(self, request, queryset):
        #queryset.update(edit=True)

@admin.register(FootNote)
class FootNoteAdmin(admin.ModelAdmin):

    list_display = ('name', 'content', 'idea', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'content')
    actions = ['approve footnotes']

    def approve_footnotes(self, request, queryset):
        queryset.update(approved=True)

    #def delete_footnotes(self, request, queryset):
        #queryset.update(deleted=True)
