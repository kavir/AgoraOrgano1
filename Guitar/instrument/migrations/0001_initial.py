# Generated by Django 4.2.2 on 2023-07-07 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ElectricGuitar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Guitar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='')),
                ('preview', models.FileField(null=True, upload_to='')),
                ('last_sold', models.DateTimeField()),
                ('Amp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='instrument.amp')),
                ('ElectricGuitar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='instrument.electricguitar')),
            ],
        ),
    ]
