# Generated by Django 3.1.2 on 2021-11-15 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModelApp', '0001_add_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prefectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'prefectures',
            },
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('prefecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelApp.prefectures')),
            ],
            options={
                'db_table': 'schools',
            },
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['-salary']},
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('major', models.CharField(max_length=20)),
                ('prefecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModelApp.prefectures')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ModelApp.schools')),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
