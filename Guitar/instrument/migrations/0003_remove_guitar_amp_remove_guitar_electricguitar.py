# Generated by Django 4.2.2 on 2023-09-28 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0002_guitar_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guitar',
            name='Amp',
        ),
        migrations.RemoveField(
            model_name='guitar',
            name='ElectricGuitar',
        ),
    ]
