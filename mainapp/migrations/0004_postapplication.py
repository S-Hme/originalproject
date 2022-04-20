# Generated by Django 4.0.1 on 2022-03-14 02:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0003_postrecruit_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_parts', models.TextField(max_length=50, verbose_name='応募パート')),
                ('a_comment', models.TextField(max_length=1000, verbose_name='コメント')),
                ('a_created_at', models.DateTimeField(auto_now_add=True)),
                ('a_author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='応募したユーザー')),
            ],
        ),
    ]
