from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class WriterProfile(models.Model):
    """
    A user profile model for writers
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20,
                              null=True, blank=True)
    default_country = CountryField(blank_label='Country *',
                                   null=True, blank=True)
    writingtype = models.CharField(max_length=20, null=True, blank=True)
    genre = models.CharField(max_length=40, null=True, blank=True)
    favouriteauthor = models.CharField(max_length=80,
                                       null=True, blank=True)
 
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        WriterProfile.objects.create(user=instance)
        # Existing users: just save the profile
    instance.writerprofile.save()
