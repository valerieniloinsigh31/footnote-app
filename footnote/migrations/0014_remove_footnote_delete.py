# Generated by Django 3.2.18 on 2023-06-24 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footnote', '0013_auto_20230624_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footnote',
            name='delete',
        ),
    ]
