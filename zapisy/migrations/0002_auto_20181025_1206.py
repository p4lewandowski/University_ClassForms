# Generated by Django 2.1.2 on 2018-10-25 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zapisy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nauczyciel',
            options={'verbose_name_plural': 'nauczyciele'},
        ),
        migrations.AlterModelOptions(
            name='przedmiot',
            options={'verbose_name_plural': 'przedmioty'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'studenci'},
        ),
    ]