# Generated by Django 4.2.2 on 2023-09-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0004_alter_guitar_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitar',
            name='discount',
            field=models.IntegerField(null=True),
        ),
    ]
