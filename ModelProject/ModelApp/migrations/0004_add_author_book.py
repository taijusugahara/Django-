# Generated by Django 3.1.2 on 2021-11-15 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelApp', '0003_add_place_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('authors', models.ManyToManyField(to='ModelApp.Authors')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
