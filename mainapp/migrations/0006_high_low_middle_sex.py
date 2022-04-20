# Generated by Django 4.0.1 on 2022-04-02 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_postapplication_a_target'),
    ]

    operations = [
        migrations.CreateModel(
            name='High',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hightone', models.CharField(max_length=10, verbose_name='高音域')),
            ],
        ),
        migrations.CreateModel(
            name='Low',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lowtone', models.CharField(max_length=10, verbose_name='低音域')),
            ],
        ),
        migrations.CreateModel(
            name='Middle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middletone', models.CharField(max_length=10, verbose_name='中音域')),
            ],
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=10, verbose_name='性別')),
            ],
        ),
    ]
