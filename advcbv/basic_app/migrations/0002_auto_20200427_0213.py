# Generated by Django 3.0.5 on 2020-04-26 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='agr',
            new_name='age',
        ),
    ]
