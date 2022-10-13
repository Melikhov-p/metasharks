from django.db import models


class Brand(models.Model):
    name = models.TextField(verbose_name='Название')

    class Meta:
        db_table = 'brand'
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.TextField(verbose_name='Название')

    class Meta:
        db_table = 'color'
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.TextField()
    brand = models.ForeignKey(Brand, verbose_name='Марка', related_name='brand', on_delete=models.CASCADE)

    class Meta:
        db_table = 'model'
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.name


class Order(models.Model):
    color = models.ForeignKey(Color, verbose_name='Цвет', on_delete=models.CASCADE)
    model = models.ForeignKey(Model, verbose_name='Модель', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name='Марка', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата')

    class Meta:
        managed = False
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
