from django.db import models


class Position(models.Model):
    """
    Модель должностей сотрудников
    """
    name = models.CharField(max_length=100, verbose_name='Название должности')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['name']

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    Модель сотрудников
    """
    surname = models.CharField(max_length=30 , verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Должность')
    date_of_employment = models.DateField(verbose_name='Дата принятия на работу')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['surname', 'name']