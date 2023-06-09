# Generated by Django 3.2.18 on 2023-06-25 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('footnote', '0015_idea_user_profile'),
        ('writer_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medley',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=280)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medley', to='footnote.idea')),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='writerprofile2', to='writer_profile.writerprofile')),
            ],
        ),
    ]
