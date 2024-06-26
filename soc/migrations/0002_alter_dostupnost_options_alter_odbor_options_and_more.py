# Generated by Django 4.2.13 on 2024-05-31 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dostupnost',
            options={'verbose_name': 'Dostupnosť', 'verbose_name_plural': 'Dostupnosti'},
        ),
        migrations.AlterModelOptions(
            name='odbor',
            options={'ordering': ['nazov'], 'verbose_name': 'Odbor', 'verbose_name_plural': 'Odbory'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['priezvisko'], 'verbose_name': 'Študent', 'verbose_name_plural': 'Študenti'},
        ),
        migrations.AlterModelOptions(
            name='tema',
            options={'ordering': ['nazov'], 'verbose_name': 'Téma', 'verbose_name_plural': 'Témy'},
        ),
        migrations.AlterModelOptions(
            name='ucitel',
            options={'ordering': ['priezvisko'], 'verbose_name': 'Učiteľ', 'verbose_name_plural': 'Učitelia'},
        ),
    ]
