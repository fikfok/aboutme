from django.db import models

class Cities(models.Model):
    cityName = models.CharField(verbose_name='Город нахождения стула', max_length=50)
    description = models.TextField(verbose_name='Описание города')
    photo = models.CharField(verbose_name='Фотография города', max_length=100)

class Personages(models.Model):
    firstName = models.CharField(verbose_name='Имя', max_length=50)
    secondName = models.CharField(verbose_name='Фамилия', max_length=50)

class Work(models.Model):
    chairNumber = models.PositiveSmallIntegerField(verbose_name='Номмер стула', unique=True)
    cityName = models.ForeignKey(Cities, verbose_name='Город нахождения стула')
    description = models.TextField(verbose_name='Краткое описание действия')
    personages = models.ManyToManyField(Personages, verbose_name='Персонажи')
    result = models.BooleanField(verbose_name='Драгоценности найдены')

    def __str__(self):
        return '{0} {1}'.format(self.chairNumber, 'стул')

class Quotes(models.Model):
    title = models.CharField(verbose_name='Заголовок цитаты', max_length=50)
    link = models.CharField(verbose_name='Ссылка', max_length=500)
    def __str__(self):
        return self.title