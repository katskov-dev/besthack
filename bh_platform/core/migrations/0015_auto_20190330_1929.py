# Generated by Django 2.1.7 on 2019-03-30 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20190330_1914'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventmodel',
            options={'permissions': (('manage', 'Право на редактирование мероприятия '),), 'verbose_name': 'Мероприятие', 'verbose_name_plural': 'Мероприятия'},
        ),
        migrations.AlterModelOptions(
            name='taskmodel',
            options={'permissions': (('manage', 'Право на редактирование задачи '),), 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]
