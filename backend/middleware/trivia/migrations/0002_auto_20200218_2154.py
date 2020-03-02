# Generated by Django 2.2.1 on 2020-02-18 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='content',
            field=models.CharField(default='empty', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='question',
            name='genre',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]