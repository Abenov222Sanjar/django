# Generated by Django 3.1.7 on 2021-03-20 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Название списка')),
            ],
            options={
                'verbose_name': 'Список',
                'verbose_name_plural': 'Списки',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(blank=True, max_length=30, null=True, verbose_name='Задача')),
                ('created', models.DateField(verbose_name='Создан')),
                ('due_on', models.DateField(verbose_name='До')),
                ('owner', models.CharField(blank=True, max_length=30, null=True, verbose_name='Автор')),
                ('mark', models.BooleanField(verbose_name='Выполнено')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='задачи', to='main.list', verbose_name='Список')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]