# Generated by Django 4.2.7 on 2023-11-14 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['surname', 'name'], 'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['name'], 'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
    ]
