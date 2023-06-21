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
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='idea_like', blank=True)

    class Meta():
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class FootNote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='footnotes')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    content = models.TextField(max_length=280)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='footnote_like', blank=True)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    class Meta():
        ordering = ['-created_on']

    def __str__(self):
        return f"FootNote {self.content} by {self.name}"

    def _generate_footnote_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update total footnotes each time a footnote is added,

        """
        self.total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.footnote_number:
            self.footnote_number = self._generate_footnote_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.footnote_number


class FootNoteLineItem(models.Model):
    """
    Line item  that represents an individual item or footnote within an idea
    """
    footnote = models.ForeignKey(FootNote, null=False, blank=False,
                                 on_delete=models.CASCADE,
                                 related_name='lineitems')
    idea = models.ForeignKey(Idea, null=False, blank=False, 
                             on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6,
                                         decimal_places=2, null=False,
                                         blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the footnote total.
        """
        self.lineitem_total = self.idea * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Idea {self.idea.name} has received {self.footnote.footnote_number} footnotes'