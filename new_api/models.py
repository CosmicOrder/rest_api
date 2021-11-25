from django.core.exceptions import ValidationError
from django.db import models


class SomeObject(models.Model):
    class Meta:
        verbose_name = 'Таблица объектов'
        verbose_name_plural = 'Таблицы объектов'

    OBJECT_TYPES = [
        ('FOLDER', 'Папка'),
        ('TYPE_1', 'тип1'),
        ('TYPE_2', 'тип2'),
    ]

    name = models.CharField(max_length=255, verbose_name='имя объекта')
    object_type = models.CharField(max_length=6, choices=OBJECT_TYPES, verbose_name='тип объекта', default='TYPE_1')
    parent_object = models.ForeignKey('SomeObject', blank=True, null=True, on_delete=models.CASCADE,
                                      related_name='child', verbose_name='родительский объект')

    def __str__(self):
        return f'{self.id}: {self.name}|{self.get_object_type_display()}'

    def clean(self):
        if self.parent_object and self.parent_object.object_type != 'FOLDER':
            raise ValidationError(message='Родительский объект не является папкой')
        return super().clean()

