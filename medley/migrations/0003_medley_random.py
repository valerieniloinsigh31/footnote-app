# Generated by Django 3.2.18 on 2023-07-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medley', '0002_auto_20230625_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medley_random',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=280)),
            ],
        ),
    ]
