from django.db import models

# Create your models here.


class List(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Название списка")

    class Meta:
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'

    def __str__(self):
        return self.name


class Todo(models.Model):
    list = models.ForeignKey(List, on_delete=models.RESTRICT, related_name='задачи', verbose_name='Список')
    todo = models.CharField(max_length=30, null=True, blank=True, verbose_name="Задача")
    created = models.DateField(verbose_name="Создан", auto_now_add=True)
    due_on = models.DateField(verbose_name="До", auto_now_add=True)
    owner = models.CharField(max_length=30, null=True, blank=True, verbose_name="Автор")
    mark = models.BooleanField(verbose_name="Выполнено")

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.todo
