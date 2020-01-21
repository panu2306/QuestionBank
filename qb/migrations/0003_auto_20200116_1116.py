# Generated by Django 3.0.1 on 2020-01-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qb', '0002_auto_20200114_0637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='lang',
        ),
        migrations.AddField(
            model_name='choice',
            name='lang',
            field=models.ManyToManyField(to='qb.Language'),
        ),
        migrations.RemoveField(
            model_name='question',
            name='lang',
        ),
        migrations.AddField(
            model_name='question',
            name='lang',
            field=models.ManyToManyField(to='qb.Language'),
        ),
    ]