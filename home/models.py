from django.db import models

class Work(models.Model):
    chairNumber = models.PositiveSmallIntegerField(verbose_name='Номмер стула', unique=True)
    cityName = models.CharField(verbose_name='Город нахождения стула', max_length=50)
    description = models.TextField(verbose_name='Краткое описание действия')
    personages = models.CharField(verbose_name='Персонажи', max_length=50)
    result = models.BooleanField(verbose_name='Драгоценности найдены')

    def __str__(self):
        return '{0} {1}'.format(self.chairNumber, 'стул')

class Quotes(models.Model):
    title = models.CharField(verbose_name='Заголовок цитаты', max_length=50)
    link = models.CharField(verbose_name='Ссылка', max_length=500)
    def __str__(self):
        return self.title