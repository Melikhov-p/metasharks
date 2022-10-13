# Generated by Django 4.1.2 on 2022-10-12 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Заказ №')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Заказ',
                'db_table': 'order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Марка',
                'db_table': 'brand',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Цвет',
                'db_table': 'color',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sharks_api.brand', verbose_name='Марка')),
            ],
            options={
                'verbose_name': 'Модель',
                'db_table': 'model',
            },
        ),
    ]
