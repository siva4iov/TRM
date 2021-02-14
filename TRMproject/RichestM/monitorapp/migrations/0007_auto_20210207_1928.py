# Generated by Django 3.1.6 on 2021-02-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitorapp', '0006_person_industry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('-fortune',), 'verbose_name': 'Миллиардер', 'verbose_name_plural': 'Миллиардеры'},
        ),
        migrations.AddField(
            model_name='photos',
            name='img',
            field=models.ImageField(null=True, unique=True, upload_to=''),
        ),
    ]
