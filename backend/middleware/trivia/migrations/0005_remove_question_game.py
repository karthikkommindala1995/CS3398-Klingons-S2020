# Generated by Django 2.2.1 on 2020-02-18 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0004_auto_20200218_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='game',
        ),
    ]