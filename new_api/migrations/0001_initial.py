# Generated by Django 3.2.9 on 2021-11-25 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SomeObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='имя объекта')),
                ('object_type', models.CharField(choices=[('FOLDER', 'Папка'), ('TYPE_1', 'тип1'), ('TYPE_2', 'тип2')], default='TYPE_1', max_length=6, verbose_name='тип объекта')),
                ('parent_object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='new_api.someobject', verbose_name='родительский объект')),
            ],
            options={
                'verbose_name': 'Таблица объектов',
                'verbose_name_plural': 'Таблицы объектов',
            },
        ),
    ]
