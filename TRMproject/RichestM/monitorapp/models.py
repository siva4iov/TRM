from django.db import models


class Citizenship(models.Model):
    title = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Гражданство'
        verbose_name_plural = 'Гражданства'


class Industry(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Сфера производства'
        verbose_name_plural = 'Cферы производства'


class Photos(models.Model):
    persons = models.ForeignKey('Person', on_delete=models.DO_NOTHING, blank=True, default=None)
    img = models.ImageField(unique=True, null=True)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Person(models.Model):
    name = models.CharField(max_length=50, unique=True)
    dob = models.DateField(verbose_name='Дата рождения')
    fortune = models.PositiveBigIntegerField(verbose_name='Состояние')
    miniature = models.ImageField(upload_to='miniatures/')
    short_description = models.CharField(max_length=255, verbose_name='Краткое описание', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True, )
    company_name = models.CharField(verbose_name='Название компании', max_length=50)
    slug = models.SlugField(unique=True)
    citizenship = models.ForeignKey(Citizenship, on_delete=models.PROTECT, null=True)
    industry = models.ManyToManyField(Industry, verbose_name='Сфера')
    rub = models.PositiveBigIntegerField(null=True)
    air = models.PositiveBigIntegerField(null=True)
    doshirak = models.PositiveBigIntegerField(null=True)
    weed = models.PositiveBigIntegerField(null=True)
    palace = models.IntegerField(null=True)
    iphone = models.PositiveBigIntegerField(null=True)
    tesla = models.IntegerField(null=True)
    falcon = models.IntegerField(null=True)
    lenin = models.IntegerField(null=True)
    janitor = models.PositiveBigIntegerField(null=True)
    krepost = models.PositiveBigIntegerField(null=True)
    cocain = models.PositiveBigIntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-fortune',)
        verbose_name = 'Миллиардер'
        verbose_name_plural = 'Миллиардеры'
