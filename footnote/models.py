from django.db import models
import uuid
from django.db.models import Sum
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from writer_profile.models import WriterProfile

STATUS = ((0, "Draft"),  (1, "Published"))


class Idea(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=500)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)
    user_profile = models.ForeignKey(WriterProfile,
                                     on_delete=models.SET_NULL, null=True,
                                     blank=True,
                                     related_name='writerprofileidea')
    delete = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        User, related_name='idea_like', blank=True)

    class Meta():
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def delete_idea(self):
        return self.idea.delete()


class FootNote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE,
                             related_name='footnotes')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    content = models.TextField(max_length=280)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='footnote_like',
                                   blank=True)
    user_profile = models.ForeignKey(WriterProfile,
                                     on_delete=models.SET_NULL, null=True,
                                     blank=True, related_name='writerprofile')

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    class Meta():
        ordering = ['-created_on']

    def __str__(self):
        return f"FootNote {self.content} by {self.name}"
