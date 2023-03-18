# Generated by Django 3.2.18 on 2023-03-18 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('footnote', '0002_rename_post_footnote_idea'),
    ]

    operations = [
        migrations.AddField(
            model_name='footnote',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='footnote_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='footnote',
            name='body',
            field=models.TextField(max_length=280),
        ),
        migrations.AlterField(
            model_name='idea',
            name='idea',
            field=models.ForeignKey(max_length=280, on_delete=django.db.models.deletion.CASCADE, related_name='idea', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='idea',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='idea_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='idea',
            name='slug',
            field=models.SlugField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='title',
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.CreateModel(
            name='Medley',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medley', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medley', to='footnote.idea')),
            ],
        ),
    ]
