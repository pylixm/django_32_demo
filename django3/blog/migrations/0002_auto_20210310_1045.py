# Generated by Django 3.2b1 on 2021-03-10 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='views',
        ),
    ]
