# Generated by Django 4.2.2 on 2023-09-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='discount',
            field=models.IntegerField(null=True),
        ),
    ]
