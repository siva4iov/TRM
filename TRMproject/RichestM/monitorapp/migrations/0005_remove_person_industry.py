# Generated by Django 3.1.6 on 2021-02-07 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitorapp', '0004_auto_20210207_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='industry',
        ),
    ]