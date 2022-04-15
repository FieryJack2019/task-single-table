from django.db import models


class TableModel(models.Model):
    date = models.DateField(verbose_name='Дата')
    name = models.CharField(max_length=100, verbose_name='Название')
    count = models.IntegerField(verbose_name='Количество')
    distance = models.FloatField(verbose_name='Расстояние')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Строка в таблице'
        verbose_name_plural = 'Строки в таблице'


