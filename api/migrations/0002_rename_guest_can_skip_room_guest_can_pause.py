# Generated by Django 4.1.7 on 2023-04-05 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='guest_can_skip',
            new_name='guest_can_pause',
        ),
    ]
