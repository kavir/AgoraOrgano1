# Generated by Django 4.2.2 on 2023-09-28 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0011_remove_guitar_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitar',
            name='price',
            field=models.IntegerField(),
        ),
    ]
