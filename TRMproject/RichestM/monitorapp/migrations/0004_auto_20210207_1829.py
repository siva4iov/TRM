# Generated by Django 3.1.6 on 2021-02-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitorapp', '0003_auto_20210207_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='industry',
            field=models.ManyToManyField(to='monitorapp.Industry', verbose_name='Сфера'),
        ),
    ]
