# Generated by Django 4.2.13 on 2024-06-07 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soc', '0004_alter_dostupnost_nazov'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tema',
            old_name='dostupnosť',
            new_name='dostupnost',
        ),
    ]
