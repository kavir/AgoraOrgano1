# Generated by Django 4.2.2 on 2023-09-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0015_remove_guitar_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='discount',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]