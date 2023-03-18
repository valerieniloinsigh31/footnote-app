from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1,"Published"))

class Idea(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='idea_like', blank=True)
    
    class Meta():
        ordering = ['-created_on']

    def __str__ (self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class FootNote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='footnotes')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(max_length=280)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='footnote_like', blank=True)

    def __str__ (self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
    

    class Meta():
        ordering = ['-created_on']

    def __str__ (self):
        return f"FootNote {self.body} by {self.name}"

