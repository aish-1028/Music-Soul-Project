# Generated by Django 3.1.1 on 2020-09-20 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enroll',
            old_name='msg',
            new_name='message',
        ),
    ]