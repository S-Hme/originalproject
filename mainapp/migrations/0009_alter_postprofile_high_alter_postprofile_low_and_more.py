# Generated by Django 4.0.1 on 2022-05-07 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0008_postprofile_high_postprofile_low_postprofile_middle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postprofile',
            name='high',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.high', verbose_name='高音域'),
        ),
        migrations.AlterField(
            model_name='postprofile',
            name='low',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.low', verbose_name='低音域'),
        ),
        migrations.AlterField(
            model_name='postprofile',
            name='middle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.middle', verbose_name='中音域'),
        ),
        migrations.AlterField(
            model_name='postprofile',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.sex', verbose_name='性別'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.postrecruit', verbose_name='投稿')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Likeしたユーザー')),
            ],
        ),
    ]