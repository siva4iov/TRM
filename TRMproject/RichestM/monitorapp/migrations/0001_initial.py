# Generated by Django 3.1.6 on 2021-02-07 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citizenship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Гражданство',
                'verbose_name_plural': 'Гражданства',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Сфера производства',
                'verbose_name_plural': 'Cферы производства',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('dob', models.DateField(verbose_name='Дата рождения')),
                ('fortune', models.PositiveBigIntegerField(verbose_name='Состояние')),
                ('miniature', models.ImageField(upload_to='miniatures/')),
                ('short_description', models.CharField(blank=True, max_length=255, verbose_name='Краткое описание')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('company_name', models.CharField(max_length=50, verbose_name='Название компании')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Миллиардер',
                'verbose_name_plural': 'Миллиардеры',
                'ordering': ('fortune',),
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persons', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='monitorapp.person')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
    ]